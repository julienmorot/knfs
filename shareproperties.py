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

from sharepropertiesdesign import *
from qt import *
from nfsData import *

class PropertiesWin(DialogProperties):

    def __init__(self, listViewNfsExports, parent = None,name = None,modal = 0,fl = 0):
        DialogProperties.__init__(self,parent,name,modal,fl)
        self.NewExport = nfsData(listViewNfsExports)
##      Now, nfs export are sync by default
        self.CheckSyncWrite.setChecked(1)

    def ButtonBrowse_clicked(self):       
        path = QFileDialog.getExistingDirectory(None, None, None, self.trUtf8("Select directory"), 1, 1)
        self.lineDirectory.setText(path)

    def ButtonResolvUID_clicked(self):
        from pwd import getpwnam
        specifieduserlogin = self.LineEditUID.displayText()
        try:
            userinfo = getpwnam(str(specifieduserlogin))
            userid = QString(unicode(userinfo[2]))
            self.LineEditUID.setText(userid)
        except:
            QMessageBox.critical(None,
                self.trUtf8("Error"),
                self.trUtf8("""The submitted user does not exist!"""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)


    def ResolvGID_clicked(self):
        from grp import getgrnam
        specifiedgroupname = self.LineEditGID.displayText()
        try:
            groupinfo = getgrnam(str(specifiedgroupname))
            groupid = QString(unicode(groupinfo[2]))
            self.LineEditGID.setText(groupid)
        except:
            QMessageBox.critical(None, self.trUtf8("Error"),
                self.trUtf8("""The submitted group is not found."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)

    def Anonymous_clicked(self):
        if self.CheckAnonymous.isChecked() == 1:
            self.CheckSpecifyUID.setEnabled(1)
            self.CheckSpecifyGID.setEnabled(1)
        else:
            self.CheckSpecifyUID.setEnabled(0)
            self.CheckSpecifyGID.setEnabled(0)

    def CheckSpecifyUID_clicked(self):
        if self.CheckSpecifyUID.isChecked() == 1:
            self.LabelSpecifyUID.setEnabled(1)
            self.LineEditUID.setEnabled(1)
            self.ButtonResolvUID.setEnabled(1)
        else:
            self.LabelSpecifyUID.setEnabled(0)
            self.LineEditUID.setEnabled(0)
            self.ButtonResolvUID.setEnabled(0)


    def CheckSpecifyGID_clicked(self):
        if self.CheckSpecifyGID.isChecked() == 1:
            self.LabelSpecifyGID.setEnabled(1)
            self.LineEditGID.setEnabled(1)
            self.ButtonResolvGID.setEnabled(1)
        else:
            self.LabelSpecifyGID.setEnabled(0)
            self.LineEditGID.setEnabled(0)
            self.ButtonResolvGID.setEnabled(0)
            
    def radioButtonreadonly_clicked(self):
        self.radioButtonReadWrite.setChecked(0)
        self.radioButtonreadonly.setChecked(1)

    def radioButtonReadWrite_clicked(self):
        self.radioButtonreadonly.setChecked(0)
        self.radioButtonReadWrite.setChecked(1)
    
    def CheckAnonymous_clicked(self):
        if self.CheckAnonymous.isChecked() == 1:
            self.CheckSpecifyUID.setEnabled(1)
            self.CheckSpecifyGID.setEnabled(1)
        else:
            self.CheckSpecifyUID.setEnabled(0)
            self.CheckSpecifyGID.setEnabled(0)

## This function parse the dialog
## and set the new export entry according to the user choice
    def buttonOk_clicked(self):
        ## We have to verify if the path is valid.
        import os
        pathexport = unicode(self.lineDirectory.displayText())
        try:
            os.listdir(pathexport)
        except:
            QMessageBox.critical(None,
                self.trUtf8("Error"),
                self.trUtf8("""The submitted path is not valid."""),
                self.trUtf8("&OK"),
                None,
                None,
                0, -1)
            return
        self.NewExport.set_directory(pathexport)


        if unicode(self.lineHosts.displayText()) != "":
            self.NewExport.set_hosts(unicode(self.lineHosts.displayText()))
        else :
            QMessageBox.critical(None,
                self.trUtf8("Error"),
                self.trUtf8("""Please submit a host."""),
                None,
                None,
                None,
                0, -1)

        if self.radioButtonreadonly.isChecked() == 1:
            self.NewExport.set_permissions("ro")
        else:
            self.NewExport.set_permissions("rw")

        if self.CheckPort1024.isChecked() == 1:
            self.NewExport.set_insecure("insecure")

        if self.CheckFileLock.isChecked() == 1:
            self.NewExport.set_insecure_locks("insecure_locks")
        
        if self.CheckDisableSubtree.isChecked() == 1:
            self.NewExport.set_no_subtree_check("no_subtree_check")
        
        if self.CheckSyncWrite.isChecked() == 1:
            self.NewExport.set_sync("sync")
        else:
            self.NewExport.set_sync("async")
        
        if self.CheckForceSync.isChecked() == 1:
            self.NewExport.set_no_wdelay("no_wdelay")
        
        if self.CheckRoot.isChecked() == 1:
            self.NewExport.set_no_root_squash("no_root_squash")
        else:
            self.NewExport.set_no_root_squash("root_squash")
        
        if self.CheckAnonymous.isChecked() == 1:
            self.NewExport.set_all_squash("all_squash")
        
        if self.CheckAnonymous.isChecked() == 1 and self.CheckSpecifyUID.isChecked() == 1:
            self.NewExport.set_anonuid(unicode(self.LineEditUID.displayText()))

        if self.CheckAnonymous.isChecked() == 1 and self.CheckSpecifyGID.isChecked() == 1:
            self.NewExport.setanongid(unicode(self.LineEditGID.displayText()))

    def get_NfsDataObject(self):
        return self.NewExport
