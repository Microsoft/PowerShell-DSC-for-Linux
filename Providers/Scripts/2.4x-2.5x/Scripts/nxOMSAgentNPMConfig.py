#!/usr/bin/env python
# ===================================
# Copyright (c) Microsoft Corporation. All rights reserved.
# See license.txt for license information.
# ===================================

import socket
import os
import sys
import imp
import md5
import codecs
import base64
import platform
import shutil
protocol = imp.load_source('protocol', '../protocol.py')
nxDSCLog = imp.load_source('nxDSCLog', '../nxDSCLog.py')
LG = nxDSCLog.DSCLog

# Paths
CONFIG_PATH = '/etc/opt/microsoft/omsagent/conf/'
SERVER_ADDRESS = '/var/opt/microsoft/omsagent/run/npmdagent.sock'
DEST_FILE_NAME = 'npmd_agent_config.xml'
PLUGIN_PATH = '/opt/microsoft/omsagent/plugin/'
PLUGIN_CONF_PATH = '/etc/opt/microsoft/omsagent/conf/omsagent.d/'
RESOURCE_MODULE_PATH = '/opt/microsoft/omsconfig/modules/nxOMSAgentNPMConfig/DSCResources/MSFT_nxOMSAgentNPMConfigResource/NPM/'
DSC_RESOURCE_VERSION_PATH = '/opt/microsoft/omsconfig/modules/nxOMSAgentNPMConfig/VERSION'
AGENT_RESOURCE_VERSION_PATH = '/var/opt/microsoft/omsagent/state/npm_version'
DSC_X64_AGENT_PATH = 'Agent/64/'
DSC_X86_AGENT_PATH = 'Agent/32/'
DSC_PLUGIN_PATH = 'Plugin/plugin/'
DSC_PLUGIN_CONF_PATH = 'Plugin/conf/'
AGENT_BINARY_PATH = '/opt/microsoft/omsagent/plugin/'
AGENT_SCRIPT_PATH = '/opt/microsoft/omsconfig/Scripts/NPMAgentBinaryCap.sh'

# Constants
X64 = '64bit'
def enum(**enums):
    return type('Enum', (), enums)
Commands = enum(LogNPM = 'ErrorLog', StartNPM = 'StartNPM', StopNPM = 'StopNPM', Config = 'Config', Purge = 'Purge')
LogType  = enum(Error = 'ERROR', Info = 'INFO')

class IOMSAgent:
    def restart_oms_agent(self):
        pass

class OMSAgentUtil(IOMSAgent):
    def restart_oms_agent(self):
        if os.system('sudo /opt/microsoft/omsagent/bin/service_control restart') == 0:
            return True
        else:
            LG().Log(LogType.Info, 'Error restarting omsagent.')
            return False

class INPMAgent:
    def binary_setcap(self):
        pass

class NPMAgentUtil(IOMSAgent):
    def binary_setcap(self, binaryPath):
        if os.path.exists(AGENT_SCRIPT_PATH) and os.system('sudo %s %s' %(AGENT_SCRIPT_PATH, binaryPath)) == 0:
            return True
        else:
            LG().Log(LogType.Error, 'Error setting capabilities to npmd agent binary.')
            return False

class INPMDiagnosticLog:
    def log(self):
        pass

class NPMDiagnosticLogUtil(INPMDiagnosticLog):
    def log(self, logType, logString):
        # Create a UDS socket
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        try:
            try:
                # Connect the socket to the port where the server is listening
                sock.connect(SERVER_ADDRESS)

                # Send data
                message = Commands.LogNPM + ':' + '[' + logType + ']' + logString
                LG().Log(logType, 'sent to NPM: ' + message)
                sock.sendall(messageNPM)
            except Exception, msg:
                LG().Log(LogType.Error, str(msg))
        finally:
            sock.close()

global show_mof
show_mof = False

OMS_ACTION = OMSAgentUtil()
NPM_ACTION = NPMAgentUtil()
LOG_ACTION = NPMDiagnosticLogUtil()

#   [key] string ConfigType;
#   [write] string ConfigID;
#   [write] string Contents;
#   [write,ValueMap{"Present", "Absent"},Values{"Present", "Absent"}] string Ensure;
#   [write] string ContentChecksum;

def init_vars(ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    if ConfigType is not None and ConfigType != '':
        ConfigType = ConfigType.encode('ascii', 'ignore')
    else:
        ConfigType = 'UpdatedAgentConfig'
    if ConfigID is not None:
        ConfigID = ConfigID.encode('ascii', 'ignore')
    else:
        ConfigID = ''
    if Contents is not None:
        Contents = base64.b64decode(Contents)#Contents.encode('ascii', 'ignore')
    else:
        Contents = ''
    if Ensure is not None and Ensure != '':
        Ensure = Ensure.encode('ascii', 'ignore')
    else:
        Ensure = 'Present'
    if ContentChecksum is not None:
        ContentChecksum = ContentChecksum.encode('ascii', 'ignore')
    else:
        ContentChecksum = ''
    return ConfigType, ConfigID, Contents, Ensure, ContentChecksum


def Set_Marshall(ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    recvdContentChecksum = md5.md5(Contents).hexdigest().upper()
    if recvdContentChecksum != ContentChecksum:
        # data is corrupt do not proceed further
        LOG_ACTION.log(LogType.Error, 'Content received did not match checksum, exiting Set')
        return [-1]
    (ConfigType, ConfigID, Contents, Ensure, ContentChecksum) = init_vars(ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    retval = Set(ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    return retval


def Test_Marshall(ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    recvdContentChecksum = md5.md5(Contents).hexdigest().upper()
    if recvdContentChecksum != ContentChecksum:
        # data is corrupt do not proceed further
        LOG_ACTION.log(LogType.Error, 'Content received did not match checksum, exiting Test')
        return [0]
    (ConfigType, ConfigID, Contents, Ensure, ContentChecksum) = init_vars(ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    retval = Test(ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    return retval


def Get_Marshall(ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    arg_names = list(locals().keys())
    (ConfigType, ConfigID, Contents, Ensure, ContentChecksum) = init_vars(ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    retval = 0
    retval = Get(ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    
    ConfigType = protocol.MI_String(ConfigType)
    ConfigID = protocol.MI_String(ConfigID)
    Ensure = protocol.MI_String(Ensure)
    Contents = protocol.MI_String(Contents)
    ContentChecksum = protocol.MI_String(ContentChecksum)

    retd = {}
    ld = locals()
    for k in arg_names:
        retd[k] = ld[k]
    return retval, retd


############################################################
# Begin user defined DSC functions
############################################################

def SetShowMof(a):
    global show_mof
    show_mof = a


def ShowMof(op, ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    if not show_mof:
        return
    mof = ''
    mof += op + ' nxOMSAgentNPMConfig MyNPMConfig \n'
    mof += '{\n'
    mof += '    ConfigType = "' + ConfigType + '"\n'
    mof += '    ConfigID = "' + ConfigID + '"\n'
    mof += '    Contents = "' + Contents + '"\n'
    mof += '    Ensure = "' + Ensure + '"\n'
    mof += '    ContentChecksum = "' + ContentChecksum + '"\n'
    mof += '}\n'
    f = open('./test_mofs.log', 'a')
    Print(mof, file=f)
    LG().Log(LogType.Info, mof)
    f.close()


def Set(ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    ShowMof('SET', ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    retval = 0
    if ConfigType != 'UpdatedAgentConfig':
        LOG_ACTION.log(LogType.Error, 'Config type did not match, exiting set')
        return [-1]
    if Ensure == 'Absent':
        if os.path.exists(AGENT_RESOURCE_VERSION_PATH):
            LG().Log(LogType.Info, 'Ensure is absent, but resource is present, purging')
            success = PurgeSolution()
            if not success:
                retval = -1
        return [retval]

    if TestConfigUpdate(Contents) != 0:
        retval = SetConfigUpdate(Contents)

    version = TestResourceVersion()
    if version != 0:
        retval = SetFilesUpdate(version)
    return [retval]


def Test(ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    ShowMof('TEST', ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    retval = 0
    if not os.path.exists(AGENT_SCRIPT_PATH):
        LG().Log(LogType.Error, 'npmd set cap script does not exist, exiting test')
        return [retval]
    if ConfigType != 'UpdatedAgentConfig':
        LOG_ACTION.log(LogType.Error, 'Config type did not match, exiting test')
        return [retval]
    if Ensure == 'Absent':
        if os.path.exists(AGENT_RESOURCE_VERSION_PATH):
            LG().Log(LogType.Info, 'Ensure is absent, resource is present on the agent, set will purge')
            retval = -1
        return [retval]

    if TestResourceVersion() != 0 or TestConfigUpdate(Contents) != 0:
        retval = -1
    return [retval]


def Get(ConfigType, ConfigID, Contents, Ensure, ContentChecksum):
    retval = 0
    ShowMof('GET', ConfigType, ConfigID, Contents, Ensure, ContentChecksum)
    return [retval]


def Print(s, file=sys.stdout):
    file.write(s + '\n')

# Compare resource version in DSC and agent machine
# Returns 
#   0 if version is same
#   dsc version number if there is a mismatch or agent config not present
def TestResourceVersion():
    retval = 0
    dscVersion = ReadFile(DSC_RESOURCE_VERSION_PATH)
    if not os.path.exists(AGENT_RESOURCE_VERSION_PATH):
        #npmd agent is not present, copy binaries
        retval = dscVersion
    else:
        agentVersion = ReadFile(AGENT_RESOURCE_VERSION_PATH)
        if agentVersion != dscVersion:
            #version mismatch, copy binaries
            retval = dscVersion
    return retval

def TestConfigUpdate(Contents):
    retval = 0
    destFileFullPath = CONFIG_PATH.__add__(DEST_FILE_NAME)
    if not os.path.exists(CONFIG_PATH):
        LOG_ACTION.log(LogType.Error, 'CONFIG_PATH does not exist')
        retval = 0
    elif not os.path.exists(destFileFullPath):
        # Configuration does not exist, fail
        retval = -1
    else:
        origConfigData = ReadFile(destFileFullPath)
        #compare
        if origConfigData is None or origConfigData != Contents:
            retval = -1
    return retval

def SetConfigUpdate(Contents):
    destFileFullPath = CONFIG_PATH.__add__(DEST_FILE_NAME)

    # Update config after checking if directory exists
    if not os.path.exists(CONFIG_PATH):
        LOG_ACTION.log(LogType.Error, 'CONFIG_PATH does not exist')
        retval = -1
    else:
        retval = WriteFile(destFileFullPath, Contents)
        if retval == 0 and os.path.exists(AGENT_RESOURCE_VERSION_PATH): #notify server only if plugin is present
            LG().Log(LogType.Info, 'Updated the file, going to notify server')
            retval = NotifyServer(Commands.Config)
    return retval

def SetFilesUpdate(newVersion):
    retval = UpdateAgentBinary(newVersion)
    retval &= UpdatePluginFiles()
    if retval:
        return 0
    return -1

def UpdateAgentBinary(newVersion):
    retval = True
    arch = platform.architecture()
    src = ''
    if arch is not None and arch[0] == X64:
        src = RESOURCE_MODULE_PATH.__add__(DSC_X64_AGENT_PATH)
        retval &= DeleteAllFiles(src, AGENT_BINARY_PATH)
        retval &= CopyAllFiles(src, AGENT_BINARY_PATH)
    else:
        src = RESOURCE_MODULE_PATH.__add__(DSC_X86_AGENT_PATH)
        retval &= DeleteAllFiles(src, AGENT_BINARY_PATH)
        retval &= CopyAllFiles(src, AGENT_BINARY_PATH)

    # set capabilities to binary
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(AGENT_BINARY_PATH, file_name) # assuming only file in directory
        break
    retval &= NPM_ACTION.binary_setcap(full_file_name)

    # Notify ruby plugin
    #retval &= NotifyServer(Commands.RestartNPM)

    #Update version number
    if retval == True:
        WriteFile(AGENT_RESOURCE_VERSION_PATH, newVersion)
    return retval

def UpdatePluginFiles():
    retval = True

    #replace files
    retval &= DeleteAllFiles(RESOURCE_MODULE_PATH.__add__(DSC_PLUGIN_PATH), PLUGIN_PATH)
    retval &= DeleteAllFiles(RESOURCE_MODULE_PATH.__add__(DSC_PLUGIN_CONF_PATH), PLUGIN_CONF_PATH)
    retval &= CopyAllFiles(RESOURCE_MODULE_PATH.__add__(DSC_PLUGIN_PATH), PLUGIN_PATH)
    retval &= CopyAllFiles(RESOURCE_MODULE_PATH.__add__(DSC_PLUGIN_CONF_PATH), PLUGIN_CONF_PATH)

    # restart oms agent
    retval &= OMS_ACTION.restart_oms_agent()

    return retval

def CopyAllFiles(src, dest):
    try:
        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            if (os.path.isfile(full_file_name)):
                shutil.copy(full_file_name, dest)
    except:
        LOG_ACTION.log(LogType.Error, 'copy_all_files failed for src: ' + src + ' dest: ' + dest)
        return False
    return True

# Deletes all files present in both directories
def DeleteAllFiles(src, dest):
    try:
        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(dest, file_name)
            if (os.path.isfile(full_file_name)):
                os.remove(full_file_name)
    except:
        LOG_ACTION.log(LogType.Error, 'delete_all_files failed for src: ' + src + ' dest: ' + dest)
        return False
    return True

def PurgeSolution():
    # remove plugin config file so that plugin does not start again
    retval = DeleteAllFiles(RESOURCE_MODULE_PATH.__add__(DSC_PLUGIN_CONF_PATH), PLUGIN_CONF_PATH)

    # remove resource version file
    try:
        os.remove(AGENT_RESOURCE_VERSION_PATH)
    except:
        LOG_ACTION.log(LogType.Error, 'failed to remove version file')
        retval = False

    # notify ruby plugin to purge agent
    if NotifyServer(Commands.Purge) != 0:
        retval = False;

    return retval

def NotifyServer(command):
    retval = 0
    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    LG().Log(LogType.Info, 'connecting to ' +  SERVER_ADDRESS)

    try:
        try:
            # Connect the socket to the port where the server is listening
            sock.connect(SERVER_ADDRESS)

            # Send data
            message = command
            LG().Log(LogType.Info, 'sending ' + message)
            sock.sendall(message)
        except Exception, msg:
            LG().Log(LogType.Error, str(msg))
            retval = -1
    finally:
        LG().Log(LogType.Info, 'closing socket')
        sock.close()
    return retval

def WriteFile(path, contents):
    retval = 0
    try:
        dFile = open(path, 'w+')
        dFile.write(contents)
        dFile.close()
    except IOError, error:
        LOG_ACTION.log(LogType.Error, "Exception opening file " + path + " Error Code: " + str(error.errno) + " Error: " + error.message + error.strerror)
        retval = -1
    return retval

def ReadFile(path):
    content = None
    try:
        dFile = codecs.open (path, encoding = 'utf8', mode = "r")
        content = dFile.read()
        dFile.close()
    except IOError, error:
        LOG_ACTION.log(LogType.Error, "Exception opening file " + path + " Error Code: " + str(error.errno) + " Error: " + error.message + error.strerror)
    return content

