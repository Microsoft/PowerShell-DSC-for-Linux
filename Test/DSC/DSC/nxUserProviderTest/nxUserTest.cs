﻿//-----------------------------------------------------------------------
// <copyright file="nxUserTest.cs" company="Microsoft">
//     Copyright (c) Microsoft Corporation.  All rights reserved.
// </copyright>
// <author>v-mifu@microsoft.com</author>
// <description>Inherit from BaseProviderTest, override Setup(IContext ctx). </description>
//-----------------------------------------------------------------------

namespace DSC
{
    using System;
    using System.Text;
    using Infra.Frmwrk;
    using System.Collections.Generic;
    using System.IO;
    using System.Text.RegularExpressions;
    
    class nxUserTest : ProviderTestBase
    {
        private string username;
        private string initialState;

        public override void Setup(IContext ctx)
        {
            ctx.Alw("nxUserTest Setup Begin.");

            mofHelper = new UserMofHelper();

            username = ctx.Records.GetValue("username");
            initialState = ctx.Records.GetValue("initialState");

            initializeCmd = ctx.Records.GetValue("initialCmd");
            finalizeCmd = ctx.Records.GetValue("finalCmd");

            base.Setup(ctx);

            if (!propMap.ContainsKey("FullName"))
            {
                propMap["FullName"] = "";
            }

            if (!propMap.ContainsKey("Description"))
            {
                propMap["Description"] = "";
            }

            if (!propMap.ContainsKey("Password"))
            {
                propMap["Password"] = "";
            }

            if (!propMap.ContainsKey("Ensure"))
            {
                propMap["Ensure"] = "present";
            }

            if (!propMap.ContainsKey("Disabled"))
            {
                propMap["Disabled"] = "False";
            }

            if (!propMap.ContainsKey("PasswordChangeRequired"))
            {
                propMap["PasswordChangeRequired"] = "False";
            }
         
            ctx.Alw("nxUserTest Setup End."); 
        }

        #region Private Methods

        private string GetInitializeCmd(string userName, string initState)
        {
            StringBuilder command = new StringBuilder();

            command.Append(String.Format("userdel -f -r {0};", userName));

            if (initState.ToLower().Equals("present"))
            {
                command.Append(String.Format("useradd {0};", userName));
            }

            return command.ToString();
        }

        private string GetFinalizeCmd(string userName)
        {
            StringBuilder command = new StringBuilder();

            command.Append(String.Format("userdel -f -r {0};", userName));

            return command.ToString();
        }

        
        public override void Verify(IContext ctx)
        {
            ctx.Alw("Verify Begin.");

            if (String.IsNullOrWhiteSpace(psErrorMsg))
            {
                // Verify if the PowerShell cmdlets were executed without error.
                if (String.IsNullOrWhiteSpace(psHelper.ErrorMsg))
                {
                    ctx.Alw("PowerShell return 0.");
                }
                else
                {
                    throw new VarFail(psHelper.ErrorMsg);
                }

                string expectedPasswordChangeRequired = ctx.Records.GetValue("expectedPasswordChangeRequired");
                Dictionary<string, string> verificationMap = propMap;
                if (!String.IsNullOrEmpty(expectedPasswordChangeRequired))
                {
                    if (verificationMap.ContainsKey("PasswordChangeRequired"))
                    {
                        verificationMap["PasswordChangeRequired"] = expectedPasswordChangeRequired;
                    }
                }
                else
                {
                    ctx.Alw("No specified property need to be verified in varmap");
                }

                //get the Test-DscConfiguration's returnvalue
                if (psHelper.TestConfigurationReturnValue != -1)
                {
                    string expectedInstallState = ctx.Records.GetValue("expectedInstallState").ToLower();
                    ctx.Alw("The expectedInstallState:" + expectedInstallState + "\n" + "the testConfigurationReturnValude:" + Convert.ToString(psHelper.TestConfigurationReturnValue) + "\n");

                    if (psHelper.TestConfigurationReturnValue == 0)
                    {
                        if (expectedInstallState != "false")
                        {
                            throw new VarFail(string.Format(
                                "The expectedInstallState: '{0}' \n" +
                                "the testConfigurationReturnValude:'{1}'\n",
                                expectedInstallState, Convert.ToString(psHelper.TestConfigurationReturnValue)));
                        }
                    }
                    else if (psHelper.TestConfigurationReturnValue == 1)
                    {
                        if (expectedInstallState != "true")
                        {
                            throw new VarFail(string.Format(
                                "The expectedInstallState: '{0}' \n" +
                                "the testConfigurationReturnValude:'{1}'\n",
                                expectedInstallState, Convert.ToString(psHelper.TestConfigurationReturnValue)));
                        }
                    }
                    ctx.Alw("Verify End.");

                    return;
                }

                //Return from Get-DscConfiguration
                Dictionary<string, string> list = psHelper.LastPowerShellReturnValues[0];
                list.Remove("CimClass");
                list.Remove("CimInstanceProperties");
                list.Remove("CimSystemProperties");
                list.Remove("PSShowComputerName");
                list.Remove("PSComputerName");
                string rltGetDSC = "The result of Get-DscConfiguration:\n\n************************************************";
                foreach (string key in list.Keys)
                {
                    rltGetDSC = rltGetDSC + String.Format("\n{0,-20}:{1}", key, list[key]);
                }
                ctx.Alw(rltGetDSC + "\n************************************************\n");
                //Get property value from Linux
                //TBD
                //Dictionary<string, string> linuxMap = new Dictionary<string, string>();
                //linuxMap = GetLinuxValue(name, propMap);

                ///////////////////////
                Dictionary<string, string> linuxMap = GetLinuxValue(); 

                foreach (string key in list.Keys)
                {

                    if (linuxMap.ContainsKey(key))
                    {
                        string actualDescription = linuxMap[key];

                        // Check Linux property value with Get-DscConfiguration
                        if (!String.IsNullOrEmpty(actualDescription))
                        {
                            try
                            {
                                psHelper.CheckOutput(key, actualDescription);
                                ctx.Alw(String.Format("Check Get-DscConfiguration: {0} is pass", key));
                            }
                            catch (VarFail ex)
                            {
                                throw new VarFail(ex.Message);
                            }
                        }
                    }

                    if (verificationMap.ContainsKey(key))
                    {
                        string mapProperty = verificationMap[key];

                        // Check property value with Get-DscConfiguration
                        if (!String.IsNullOrEmpty(mapProperty))
                        {
                            try
                            {
                                psHelper.CheckOutput(key, mapProperty);
                                ctx.Alw(String.Format("Check Get-DscConfiguration: {0} is pass", key));
                            }
                            catch (VarFail ex)
                            {
                                throw new VarFail(ex.Message);
                            }
                        }
                    }
                }
            }
            else
            {
                psHelper.CheckErrorMessage(psErrorMsg);
                ctx.Alw(String.Format("PowerShell return error message '{0}' as expected!", psErrorMsg));
            }

            ctx.Alw("Verify End.");
        }

        protected override Dictionary<string, string> GetLinuxValue()
        {
            Dictionary<string, string> linuxValueMap = new Dictionary<string, string>();
            string userName = propMap["UserName"];
            string homeDir = propMap.ContainsKey("HomeDirectory") ? propMap["HomeDirectory"] : string.Empty;
            string ensureVal = propMap.ContainsKey("Ensure") ? propMap["Ensure"] : "present";
            string groupID = string.Empty;
            string cmd = string.Empty;
            string verifyLog = string.Empty;

            if (ensureVal.ToLower() == "present")
            {
                try
                {
                    cmd = "cat /etc/passwd |grep -i {0}: |awk '{print $1}'|cut -d ':' -f4 |tr -d '\n'";
                    string getGroupCmd = cmd.Replace("{0}", userName);

                    sshHelper.Execute(getGroupCmd, out groupID);
                }
                catch (Exception)
                {
                    throw new VarFail(String.Format("Fail to get GroupID of user: {0}", userName));
                }

                if (string.IsNullOrEmpty(homeDir))
                {
                    try
                    {
                        cmd = "ls {0}";
                        string verifyHomeDirCmd = cmd.Replace("{0}", homeDir);

                        sshHelper.Execute(verifyHomeDirCmd, out verifyLog);
                    }
                    catch (Exception)
                    {
                        throw new VarFail(String.Format("No home directory: {0}", homeDir));
                    }
                }

                linuxValueMap["HomeDirectory"] = homeDir;
                linuxValueMap["GroupID"] = groupID;
            }
            else
            {
                //if Ensure is 'absent', the value is null.
                linuxValueMap["HomeDirectory"] = "";
                linuxValueMap["GroupID"] = "";
            }

            return linuxValueMap;
        } 

        #endregion 
    }
}