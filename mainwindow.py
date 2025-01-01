## Copyright (C) 2004, Julien Morot

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

import sys
import os
import string
from mainwindowdesign import *
from nfsBackend import *
from shareproperties import *

from nfsData import *

class MainWin(MainNFSForm):

    def __init__(self, parent=None):
        MainNFSForm.__init__(self, parent)
        self.exports = NfsBackend(self.listNfsExport)
        self.exports.printItems(self.listNfsExport)

##      Hack to verify if nfs daemon rpc.mountd is active :
        output = os.popen("ps ax | grep -i rpc.mountd | grep -i bin | cut -d '/' -f 4").read()
        runningStatus = string.strip(output)
        if runningStatus == 'rpc.mountd':
            self.serviceStartAction.setEnabled(0)
            self.serviceStopAction.setEnabled(1)
        else:
            self.serviceStartAction.setEnabled(1)
            self.serviceStopAction.setEnabled(0)

    def fileNew(self):
        result = 0
        dialog = PropertiesWin(self.listNfsExport)
        result = dialog.exec_loop()
##      This check verify if the user click on OK button.
        if result == 1:
            NewNfsExportObject = dialog.get_NfsDataObject()
            self.exports.addEntry(NewNfsExportObject)
            self.exports.printItems(self.listNfsExport)
        del(dialog)
        del(result)

    def fileDelete(self):
        if self.listNfsExport.selectedItem() != None:
            itemtodelete = self.listNfsExport.selectedItem()
            self.exports.entries.remove(itemtodelete)
            self.listNfsExport.takeItem(itemtodelete)

    def fileEdit(self):
        result = 0
        if self.listNfsExport.selectedItem() != None:
            itemtomodify = self.listNfsExport.selectedItem()
            dialog = PropertiesWin(self.listNfsExport)
            
            ## Fill the dialog according to the selected nfs export :
            dialog.lineDirectory.setText(QString(itemtomodify.get_directory()))
            dialog.lineHosts.setText(QString(itemtomodify.get_hosts()))
            
            if itemtomodify.get_permissions() == "ro":
                dialog.radioButtonreadonly.setChecked(1)
                dialog.radioButtonReadWrite.setChecked(0)
            else:
                dialog.radioButtonreadonly.setChecked(0)
                dialog.radioButtonReadWrite.setChecked(1)
            
            if itemtomodify.get_insecure() == "insecure":
                dialog.CheckPort1024.setChecked(1)
            if itemtomodify.get_sync() == "sync":
                dialog.CheckSyncWrite.setChecked(1)
            if itemtomodify.get_no_wdelay() == "no_wdelay":
                dialog.CheckForceSync.setChecked(1)
            if itemtomodify.get_no_subtree_check() == "no_subtree_check":
                dialog.CheckDisableSubtree.setChecked(1)
            if itemtomodify.get_insecure_locks() == "insecure_lock":
                dialog.CheckFileLock.setChecked(1)
            if itemtomodify.get_no_root_squash() == "no_root_squash":
                dialog.CheckRoot.setChecked(1)
            if itemtomodify.get_all_squash() == "all_squash":
                dialog.CheckAnonymous.setChecked(1)
            if itemtomodify.get_anonuid() != None:
                dialog.LineEditUID.displayText(QString(itemtomodify.get_anonuid()))
            if itemtomodify.get_anongid() != None:
                dialog.LineEditGID.displayText(QString(itemtomodify.get_anongid()))

            result = dialog.exec_loop()

##      If the user click on OK button, modify the old export
        if result == 1:
            self.exports.entries.remove(itemtomodify)
            self.listNfsExport.takeItem(itemtomodify)
            self.exports.entries.append(dialog.get_NfsDataObject())
            self.exports.printItems(self.listNfsExport)
        del(dialog)
        del(itemtomodify)
        del(result)

    def fileSave(self):
        self.exports.writeFile(self.exports.entries)

    def fileExit(self):
        sys.exit(0)

    def helpAbout(self):
        print "MainWin.helpAbout(): Not implemented yet"
   
    def serviceStart(self):
##        TODO : Add a better check isn't it?
        try:
            os.system('/etc/init.d/nfs start > /dev/null')
            self.serviceStartAction.setEnabled(0)
            self.serviceStopAction.setEnabled(1)
        except:
            QMessageBox.critical(None,
                self.trUtf8("Error"),
                self.trUtf8("""Unable to restart services."""),
                None,
                None,
                None,
                0, -1)
    
    def serviceRestart(self):
##        TODO : Add a better check isn't it?
        try:
            os.system('/etc/init.d/portmap restart > /dev/null')
            os.system('/etc/init.d/nfs restart > /dev/null')
            self.serviceStartAction.setEnabled(1)
            self.serviceStopAction.setEnabled(0)
        except:
            QMessageBox.critical(None,
                self.trUtf8("Error"),
                self.trUtf8("""Unable to restart the NFS service."""),
                None,
                None,
                None,
                0, -1)

    
    def serviceStop(self):
##        TODO : Add a better check isn't it?
        try:
            os.system('/etc/init.d/nfs stop > /dev/null')
            self.serviceStopAction.setEnabled(0)
            self.serviceStartAction.setEnabled(1)
        except:
            QMessageBox.critical(None,
                self.trUtf8("Error"),
                self.trUtf8("""Unable to stop the NFS service."""),
                None,
                None,
                None,
                0, -1)

    def listNfsExport_doubleClicked(self,a0):
        self.fileEdit()

    def listNfsExport_returnPressed(self,a0):
        self.fileEdit()
