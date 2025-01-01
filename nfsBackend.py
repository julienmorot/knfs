## nfsBackend.py - Contains the backend code needed for knfs
## Based on the work of Red Hat fo system-config-nfs

## Copyright (C) 2002, 2003 Red Hat, Inc.
## Copyright (C) 2002, 2003 Brent Fox <bfox@redhat.com>

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import string
import os
import nfsData


class NfsBackend:

    def __init__(self, listViewNfsExports):
        self.entries = []
        self.parseFile(listViewNfsExports)

    def addEntry(self, nfsDataObject):
        self.entries.append(nfsDataObject)

    def getEntries(self):
        return self.entries

    def printEntries(self):
        print "Directory\tPermissions\t\tHosts"        
        for key in self.entries:
            print ("%s\t\t%s\t\t\t%s" % (key.directory, key.permissions, key.hosts))

    def startNfs(self):
        os.system('/etc/init.d/portmap restart > /dev/null')
        os.system('/etc/init.d/nfs start > /dev/null')

    def exportFs(self):
        os.system('/usr/sbin/exportfs -r')

    def writeFile(self, nfsDataObjectList):
        try:
            os.rename('/etc/exports', '/etc/exports.bak')
        except OSError:
            pass
        fd = open('/etc/exports', 'w')

        for nfsDataObject in nfsDataObjectList:
            directory = nfsDataObject.get_directory()
            line = directory

            spaceLen = 25
            
            if len(directory) < spaceLen:
                for i in range(spaceLen - len(directory)):
                    line = line + " "
            else:
                for i in range(6):
                    line = line + " "

            line = line + nfsDataObject.get_hosts()
            line = line + "("
            optionList = []

            if nfsDataObject.get_permissions():                
                optionList.append(nfsDataObject.get_permissions())
            if nfsDataObject.get_insecure():
                optionList.append(nfsDataObject.get_insecure())
            if nfsDataObject.get_sync():
                optionList.append(nfsDataObject.get_sync())
            if nfsDataObject.get_no_wdelay():
                optionList.append(nfsDataObject.get_no_wdelay())
            if nfsDataObject.get_no_subtree_check():
                optionList.append(nfsDataObject.get_no_subtree_check())
            if nfsDataObject.get_insecure_locks():
                optionList.append(nfsDataObject.get_insecure_locks())
            if nfsDataObject.get_no_root_squash():
                optionList.append(nfsDataObject.get_no_root_squash())
            if nfsDataObject.get_all_squash():
                optionList.append(nfsDataObject.get_all_squash())
            if nfsDataObject.get_anonuid():
                optionList.append("anonuid=" + str(nfsDataObject.get_anonuid()))
            if nfsDataObject.get_anongid():
                optionList.append("anongid=" + str(nfsDataObject.get_anongid()))

            optionLine = string.joinfields(optionList, ",")
            line = line + optionLine + ')\n'
            fd.write(line)

        fd.close()
        
    def parseFile(self, listViewNfsExports):
        try:
            fd = open('/etc/exports', 'r')
            lines = fd.readlines()
            fd.close ()
        except IOError:
            lines = []

        for line in lines:
            if line[0] == '#' or line == "\n":
                continue
            else:
                tokens = string.split(line)

                if len(tokens) > 2:
                    tmp = string.join(tokens[1:])
                    #This eliminates the space between host and option flags
                    tmp = string.replace(tmp, ' (', '(')
                    data = tmp
                else:
                    data = tokens[1]

                hosts = string.split(data)

                if len(hosts) == 1:
                    #Create the nfsData object
                    nfsDataObject = nfsData.nfsData(listViewNfsExports)
                    #Set the directory to be exported
                    nfsDataObject.set_directory(tokens[0])
                    self.parseOptions(nfsDataObject, data)
                    self.entries.append(nfsDataObject)
                elif len(hosts) > 1:
                    for host in hosts:
                        #Create the nfsData object
                        nfsDataObject = nfsData.nfsData(listViewNfsExports)
                        #Set the directory to be exported
                        nfsDataObject.set_directory(tokens[0])
                        self.parseOptions(nfsDataObject, host)
                        self.entries.append(nfsDataObject)

                
    def parseOptions(self, object, data):
        try:
            hostname, options = string.split(data, "(")
            options = string.replace(options, ")", "")
            optionTokens = string.split(options, ",")

            for token in optionTokens:                    
                object.set_hosts(hostname)

                if token == "ro":
                    object.set_permissions(token)
                elif token == "rw":
                    object.set_permissions(token)
                elif token == "insecure":
                    object.set_insecure(token)
                elif token == "sync" or token == "async":
                    object.set_sync(token)
                elif token == "no_wdelay":
                    object.set_no_wdelay(token)
                elif token == "no_subtree_check":
                    object.set_no_subtree_check(token)
                elif token == "insecure_locks" or token == "no_auth_nlm":
                    object.set_insecure_locks(token)
                elif token == "no_root_squash":
                    object.set_no_root_squash(token)
                elif token == "all_squash":
                    object.set_all_squash(token)
                elif token[:7] == "anonuid":
                    str, uid = string.split(token, "=")
                    object.set_anonuid(uid)
                elif token[:7] == "anongid":
                    str, gid = string.split(token, "=")
                    object.set_anongid(gid)
        except ValueError:
            # no options
            object.set_hosts(data)

##  From the list of nfs export, fill the main QListView
    def printItems(self, listViewNfsExports):
        i = 0
        for item in self.entries:
            item.set_col_directory()
            item.set_col_hosts()
            item.set_col_perms()

