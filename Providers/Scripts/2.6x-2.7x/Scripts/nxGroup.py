#!/usr/bin/env python
#============================================================================
# Copyright (c) Microsoft Corporation. All rights reserved. See license.txt for license information.
#============================================================================
#from __future__ import print_function
from __future__ import with_statement
from contextlib import contextmanager

import os
import sys
import codecs

# 	[Key] string GroupName;
# 	[write,ValueMap{"Present", "Absent"},Values{"Present", "Absent"}] string Ensure;
# 	[write] string Members[];
# 	[write] string MembersToInclude[];
# 	[write] string MembersToExclude[];
# 	[write] string PreferredGroupID;	

global show_mof
show_mof=False


def Set_Marshall(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
    if  GroupName != None :
        GroupName=GroupName.decode("utf-8")
    else:
        GroupName = ''
    if Ensure != None :
        Ensure=Ensure.decode("utf-8")
    else:
        Ensure = ''
    if Members != None :
        Members=Members.decode("utf-8")
    else:
        Members = ''
    if MembersToInclude != None :
        MembersToInclude=MembersToInclude.decode("utf-8")
    else:
        MembersToInclude = ''
    if MembersToExclude != None :
        MembersToExclude=MembersToExclude.decode("utf-8")
    else:
        MembersToExclude = ''
    if PreferredGroupID != None :
        PreferredGroupID=PreferredGroupID.decode("utf-8")
    else:
        PreferredGroupID = ''

    retval = Set(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    return retval

def Test_Marshall(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
    if GroupName != None :
        GroupName=GroupName.decode("utf-8")
    else:
        GroupName = ''
    if Ensure != None :
        Ensure=Ensure.decode("utf-8")
    else:
        Ensure = ''
    if Members != None :
        Members=Members.decode("utf-8")
    else:
        Members = ''
    if MembersToInclude != None :
        MembersToInclude=MembersToInclude.decode("utf-8")
    else:
        MembersToInclude = ''
    if MembersToExclude != None :
        MembersToExclude=MembersToExclude.decode("utf-8")
    else:
        MembersToExclude = ''
    if PreferredGroupID != None :
        PreferredGroupID=PreferredGroupID.decode("utf-8")
    else:
        PreferredGroupID = ''

    retval = Test(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    return retval

def Get_Marshall(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
    arg_names=locals().keys()
    if GroupName != None :
        GroupName=GroupName.decode("utf-8")
    else:
        GroupName = ''
    if Ensure != None :
        Ensure=Ensure.decode("utf-8")
    else:
        Ensure = ''
    if Members != None :
        Members=Members.decode("utf-8")
    else:
        Members = ''
    if MembersToInclude != None :
        MembersToInclude=MembersToInclude.decode("utf-8")
    else:
        MembersToInclude = ''
    MembersToExclude = MembersToExclude.decode("utf-8")
    PreferredGroupID = PreferredGroupID.decode("utf-8")

    retval = 0
    (retval, GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID) = Get(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)

    GroupName = GroupName.encode("utf-8")
    Ensure = Ensure.encode("utf-8")
    Members = Members.encode("utf-8")
    MembersToInclude = MembersToInclude.encode("utf-8")
    MembersToExclude = MembersToExclude.encode("utf-8")
    PreferredGroupID = PreferredGroupID.encode("utf-8")

    retd={}
    ld=locals()
    for k in arg_names :
        retd[k]=ld[k] 
    return retval, retd


############################################################
### Begin user defined DSC functions
############################################################

def SetShowMof(a):
    global show_mof
    show_mof=a

def ShowMof(op, GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
    if not show_mof:
        return
    mof=''
    mof+=op + ' nxGroup MyGroup \n'
    mof+='{\n'
    mof+='    GroupName = "' + GroupName + '"\n'
    mof+='    Ensure = "' + Ensure + '"\n'
    mof+='    Members = "' + repr(Members) + '"\n'
    mof+='    MembersToInclude = "' + repr(MembersToInclude) + '"\n'
    mof+='    MembersToExclude = "' + repr(MembersToExclude) + '"\n'
    mof+='    PreferredGroupID = "' + str(PreferredGroupID) + '"\n'
    mof+='}\n'
    f=open('./test_mofs.log','a')
    Print(mof,file=f)
    f.close()
    
def Print(s,file=sys.stdout):
    file.write(s+'\n')
    
@contextmanager
def opened_w_error(filename, mode="r"):
    """
    This context ensures the file is closed.
    """
    try:
        f = codecs.open(filename, encoding='utf-8' , mode=mode)
    except IOError, err:
        yield None, err
    else:
        try:
            yield f, None
        finally:
            f.close()


groupadd_path = "/usr/sbin/groupadd"
groupdel_path = "/usr/sbin/groupdel"
groupmod_path = "/usr/sbin/groupmod"
gpasswd_path = "/usr/bin/gpasswd"
add_user_to_group_gpasswd = gpasswd_path + " -a "
delete_user_from_group_gpasswd = gpasswd_path + " -d "
add_user_to_group_groupmod = groupmod_path + " -A "
delete_user_from_group_groupmod = groupmod_path + " -R "

add_user_to_group = add_user_to_group_gpasswd
delete_user_from_group = delete_user_from_group_gpasswd

# If gpasswd fails to let us add/remove users, try groupmod
def SwapGroupModCommand():
    global add_user_to_group
    global delete_user_from_group

    if add_user_to_group == add_user_to_group_gpasswd:
        add_user_to_group = add_user_to_group_groupmod
        delete_user_from_group = delete_user_from_group_groupmod
    else:
        add_user_to_group = add_user_to_group_gpasswd
        delete_user_from_group = delete_user_from_group_gpasswd

def ReadPasswd(filename):
    with opened_w_error(filename,'rb') as (f,error):
        if error:
            Print("Exception opening file " + filename + " Error Code: " + str(error.errno) + " Error: " + error.message + error.strerror,file=sys.stderr )
            return None
        else:
            lines = f.read().split("\n")
    
    entries = dict()
    for line in lines:
        tokens = line.split(":")
        if len(tokens) > 1:
            entries[tokens[0]] = tokens[1:]

    return entries

def ParseList(s):
    if type(s) == 'str':
        return s.strip('\n')
    else:
        return s
    
def get_GID(n):
    return int(n[1][1])

def AddUserToGroup(UserName, GroupName):
    retval = os.system(add_user_to_group + UserName + " " + GroupName)
    if retval != 0:
        SwapGroupModCommand()
        retval = os.system(add_user_to_group + UserName + " " + GroupName)
        if retval != 0:
            Print("Error adding user: " + UserName + " to group: " + GroupName,file=sys.stderr)
            return False
    return True

def DeleteUserFromGroup(UserName, GroupName):
    retval = os.system(delete_user_from_group + UserName + " " + GroupName)
    if retval != 0:
        SwapGroupModCommand()
        retval = os.system(delete_user_from_group + UserName + " " + GroupName)
        if retval != 0:
            Print("Error removing user: " + UserName + " from group: " + GroupName,file=sys.stderr)
            return False
    return True

def GetGroupMembers(GroupName, group_entries):
    group_members = group_entries[GroupName][2].split(",")
    if group_members[0] == "":
        group_members = []
    return group_members

class Params:
    def __init__(self,GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
        self.Ensure = Ensure
        self.GroupName = GroupName
        self.MembersToExclude = MembersToExclude
        self.MembersToInclude = MembersToInclude
        self.Members = Members
        self.PreferredGroupID = PreferredGroupID
        
def Set(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
    ShowMof('SET', GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    p=Params(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    if not Ensure:
        Ensure = "present"
    group_entries=None
    group_entries = ReadPasswd("/etc/group")
    if group_entries == None:
        return [-1]
    Members_list = ParseList(Members)

    if Ensure.lower() == "absent":
        if GroupName in group_entries:
            # Delete group
            Print("Deleting group",file=sys.stderr)
            retval = os.system(groupdel_path + " " + GroupName)
            if retval != 0:
                Print(groupdel_path + " " + GroupName + " failed.",file=sys.stderr)
                return [-1]
    else:
        if GroupName not in group_entries:
            Print("Group does not exist. Creating it.",file=sys.stderr)
            retval = os.system(groupadd_path + " " + GroupName)
            if retval != 0:
                Print(groupadd_path + " " + GroupName + " failed.",file=sys.stderr)
                return [-1]

            # Reread /etc/group
            group_entries = ReadPasswd("/etc/group")

        if Members:
            if MembersToInclude or MembersToExclude:
                Print("If Members is provided, Include and Exclude are not allowed.",file=sys.stderr)
                return [-1]

            group_members = GetGroupMembers(GroupName, group_entries)
            for member in Members_list:
                if member not in group_members:
                    Print("Member: " + member + " not in member list for group: " + GroupName + ".  Adding.",file=sys.stderr)
                    if AddUserToGroup(member, GroupName) == False:
                        return [-1]
            for member in group_members:
                if member not in Members_list:
                    Print("Member: " + member + " is in the member list for group: " + GroupName + " but not speficied in Members.  Removing.",file=sys.stderr)
                    if DeleteUserFromGroup(member, GroupName) == False:
                        return [-1]
                

        else:
            group_members = GetGroupMembers(GroupName, group_entries)
            if MembersToInclude:
                MembersToInclude_list = ParseList(MembersToInclude)
                for member in MembersToInclude_list:
                    if member not in group_members:
                        Print("Member: " + member + " not in member list for group: " + GroupName + ".  Adding.",file=sys.stderr)
                        if AddUserToGroup(member, GroupName) == False:
                            return [-1]
            if MembersToExclude:
                MembersToExclude_list = ParseList(MembersToExclude)
                for member in MembersToExclude_list:
                    if member in group_members:
                        Print("Member: " + member + " is in member list for group: " + GroupName + ".  Removing.",file=sys.stderr)
                        if DeleteUserFromGroup(member, GroupName) == False:
                            return [-1]
    
    return [0]


def Test(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
    ShowMof('TEST', GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    p=Params(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    if not Ensure:
        Ensure = "present"

    group_entries = ReadPasswd("/etc/group")
    Members_list = ParseList(Members)

    if Ensure.lower() == "absent":
        if GroupName not in group_entries:
            return [0]
        else:
            return [-1]
    else:
        if GroupName not in group_entries:
            Print("Group does not exist.",file=sys.stderr)
            return [-1]
        
        if Members:
            if MembersToInclude or MembersToExclude:
                Print("If Members is provided, Include and Exclude are not allowed.",file=sys.stderr)
                return [-1]

            group_members = GetGroupMembers(GroupName, group_entries)

            for member in Members_list:
                if member not in group_members:
                    Print("Member: " + member + " not in member list for group: " + GroupName,file=sys.stderr)
                    return [-1]
            for member in group_members:
                if member not in Members_list:
                    Print("Member: " + member + " is in the member list for group: " + GroupName + " but not speficied in Members",file=sys.stderr)
                    return [-1]
                
        else:
            group_members = GetGroupMembers(GroupName, group_entries)

            if MembersToInclude:
                MembersToInclude_list = ParseList(MembersToInclude)
                for member in MembersToInclude_list:
                    if member not in group_members:
                        Print("Member: " + member + " not in member list for group: " + GroupName,file=sys.stderr)
                        return [-1]
            if MembersToExclude:
                MembersToExclude_list = ParseList(MembersToExclude)
                for member in MembersToExclude_list:
                    if member in group_members:
                        Print("Member: " + member + " is in member list for group: " + GroupName,file=sys.stderr)
                        return [-1]

    return [0]


def Get(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID):
    ShowMof('GET', GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    p=Params(GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID)
    group_entries = ReadPasswd("/etc/group")
    Members = MembersToInclude = MembersToExclude = ""

    if GroupName not in group_entries:
        Ensure = "Absent"
        PreferredGroupID = ""
    else:
        Ensure = "Present"
        PreferredGroupID = group_entries[GroupName][1]
        Members = GetGroupMembers(GroupName, group_entries)

    return [0, GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID]

