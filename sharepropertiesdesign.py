# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shareproperties.ui'
#
# Created: sam mar 5 15:40:36 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DialogProperties(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("DialogProperties")

        self.setSizeGripEnabled(1)
        self.setModal(1)


        LayoutWidget = QWidget(self,"Layout5")
        LayoutWidget.setGeometry(QRect(500,30,82,410))
        Layout5 = QVBoxLayout(LayoutWidget,0,6,"Layout5")

        self.buttonOk = QPushButton(LayoutWidget,"buttonOk")
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout5.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(LayoutWidget,"buttonCancel")
        self.buttonCancel.setAutoDefault(1)
        Layout5.addWidget(self.buttonCancel)
        Spacer1 = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        Layout5.addItem(Spacer1)

        self.groupBoxOptions = QGroupBox(self,"groupBoxOptions")
        self.groupBoxOptions.setGeometry(QRect(10,160,480,280))

        self.CheckPort1024 = QCheckBox(self.groupBoxOptions,"CheckPort1024")
        self.CheckPort1024.setGeometry(QRect(10,20,460,21))

        self.CheckSyncWrite = QCheckBox(self.groupBoxOptions,"CheckSyncWrite")
        self.CheckSyncWrite.setGeometry(QRect(10,80,460,21))

        self.CheckForceSync = QCheckBox(self.groupBoxOptions,"CheckForceSync")
        self.CheckForceSync.setGeometry(QRect(10,100,460,21))

        self.lineOptions = QFrame(self.groupBoxOptions,"lineOptions")
        self.lineOptions.setGeometry(QRect(10,120,460,20))
        self.lineOptions.setFrameShape(QFrame.HLine)
        self.lineOptions.setFrameShadow(QFrame.Sunken)
        self.lineOptions.setFrameShape(QFrame.HLine)

        self.CheckRoot = QCheckBox(self.groupBoxOptions,"CheckRoot")
        self.CheckRoot.setGeometry(QRect(10,140,460,20))

        self.CheckDisableSubtree = QCheckBox(self.groupBoxOptions,"CheckDisableSubtree")
        self.CheckDisableSubtree.setGeometry(QRect(10,60,460,21))

        self.LineEditGID = QLineEdit(self.groupBoxOptions,"LineEditGID")
        self.LineEditGID.setEnabled(0)
        self.LineEditGID.setGeometry(QRect(80,250,150,21))

        self.LabelSpecifyUID = QLabel(self.groupBoxOptions,"LabelSpecifyUID")
        self.LabelSpecifyUID.setEnabled(0)
        self.LabelSpecifyUID.setGeometry(QRect(10,200,61,21))

        self.LabelSpecifyGID = QLabel(self.groupBoxOptions,"LabelSpecifyGID")
        self.LabelSpecifyGID.setEnabled(0)
        self.LabelSpecifyGID.setGeometry(QRect(10,250,61,21))

        self.CheckFileLock = QCheckBox(self.groupBoxOptions,"CheckFileLock")
        self.CheckFileLock.setGeometry(QRect(10,40,460,21))

        self.CheckSpecifyGID = QCheckBox(self.groupBoxOptions,"CheckSpecifyGID")
        self.CheckSpecifyGID.setEnabled(0)
        self.CheckSpecifyGID.setGeometry(QRect(10,230,310,20))

        self.ButtonResolvUID = QPushButton(self.groupBoxOptions,"ButtonResolvUID")
        self.ButtonResolvUID.setEnabled(0)
        self.ButtonResolvUID.setGeometry(QRect(330,200,100,30))

        self.ButtonResolvGID = QPushButton(self.groupBoxOptions,"ButtonResolvGID")
        self.ButtonResolvGID.setEnabled(0)
        self.ButtonResolvGID.setGeometry(QRect(330,240,100,30))

        self.LineEditUID = QLineEdit(self.groupBoxOptions,"LineEditUID")
        self.LineEditUID.setEnabled(0)
        self.LineEditUID.setGeometry(QRect(80,200,150,21))

        self.CheckSpecifyUID = QCheckBox(self.groupBoxOptions,"CheckSpecifyUID")
        self.CheckSpecifyUID.setEnabled(0)
        self.CheckSpecifyUID.setGeometry(QRect(10,180,310,20))

        self.CheckAnonymous = QCheckBox(self.groupBoxOptions,"CheckAnonymous")
        self.CheckAnonymous.setEnabled(1)
        self.CheckAnonymous.setGeometry(QRect(10,160,460,20))

        self.groupBoxShare = QGroupBox(self,"groupBoxShare")
        self.groupBoxShare.setGeometry(QRect(10,10,480,140))

        self.LabelHosts = QLabel(self.groupBoxShare,"LabelHosts")
        self.LabelHosts.setGeometry(QRect(10,60,60,31))

        self.LabelPermissions = QLabel(self.groupBoxShare,"LabelPermissions")
        self.LabelPermissions.setGeometry(QRect(10,100,90,31))

        self.LabelDirectory = QLabel(self.groupBoxShare,"LabelDirectory")
        self.LabelDirectory.setGeometry(QRect(10,20,70,31))

        self.lineHosts = QLineEdit(self.groupBoxShare,"lineHosts")
        self.lineHosts.setGeometry(QRect(80,60,380,30))

        self.radioButtonreadonly = QRadioButton(self.groupBoxShare,"radioButtonreadonly")
        self.radioButtonreadonly.setGeometry(QRect(120,100,111,30))
        self.radioButtonreadonly.setChecked(1)

        self.radioButtonReadWrite = QRadioButton(self.groupBoxShare,"radioButtonReadWrite")
        self.radioButtonReadWrite.setGeometry(QRect(260,100,111,30))

        self.ButtonBrowse = QToolButton(self.groupBoxShare,"ButtonBrowse")
        self.ButtonBrowse.setGeometry(QRect(370,20,90,32))

        self.lineDirectory = QLineEdit(self.groupBoxShare,"lineDirectory")
        self.lineDirectory.setGeometry(QRect(80,20,270,30))

        self.languageChange()

        self.resize(QSize(592,450).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonOk,SIGNAL("clicked()"),self.accept)
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self.reject)
        self.connect(self.ButtonBrowse,SIGNAL("clicked()"),self.ButtonBrowse_clicked)
        self.connect(self.ButtonResolvUID,SIGNAL("clicked()"),self.ButtonResolvUID_clicked)
        self.connect(self.ButtonResolvGID,SIGNAL("clicked()"),self.ResolvGID_clicked)
        self.connect(self.CheckAnonymous,SIGNAL("clicked()"),self.CheckAnonymous_clicked)
        self.connect(self.CheckSpecifyUID,SIGNAL("clicked()"),self.CheckSpecifyUID_clicked)
        self.connect(self.CheckSpecifyGID,SIGNAL("clicked()"),self.CheckSpecifyGID_clicked)
        self.connect(self.radioButtonreadonly,SIGNAL("clicked()"),self.radioButtonreadonly_clicked)
        self.connect(self.radioButtonReadWrite,SIGNAL("clicked()"),self.radioButtonReadWrite_clicked)
        self.connect(self.buttonOk,SIGNAL("clicked()"),self.buttonOk_clicked)


    def languageChange(self):
        self.setCaption(self.__tr("DialogProperties"))
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonOk.setAccel(self.__tr("Alt+O"))
        self.buttonCancel.setText(self.__tr("&Cancel"))
        self.buttonCancel.setAccel(self.__tr("Alt+C"))
        self.groupBoxOptions.setTitle(self.__tr("Export Options"))
        self.CheckPort1024.setText(self.__tr("Allow connections from ports 1024 and higher"))
        self.CheckSyncWrite.setText(self.__tr("Sync write operations on request"))
        self.CheckForceSync.setText(self.__tr("Force sync of write operations immediately"))
        self.CheckRoot.setText(self.__tr("Treat remote root user as local root"))
        self.CheckDisableSubtree.setText(self.__tr("Disable subtree checking"))
        self.LabelSpecifyUID.setText(self.__tr("User ID :"))
        self.LabelSpecifyGID.setText(self.__tr("Group ID :"))
        self.CheckFileLock.setText(self.__tr("Allow insecure file locking"))
        self.CheckSpecifyGID.setText(self.__tr("Specify local group ID for anonymous users"))
        self.ButtonResolvUID.setText(self.__tr("Resolve  UID"))
        self.ButtonResolvGID.setText(self.__tr("Resolve GID"))
        self.CheckSpecifyUID.setText(self.__tr("Specify local user ID for anonymous users"))
        self.CheckAnonymous.setText(self.__tr("Treat all client users as anonymous users"))
        self.groupBoxShare.setTitle(self.__tr("Share"))
        self.LabelHosts.setText(self.__tr("Hosts :"))
        self.LabelPermissions.setText(self.__tr("Permissions :"))
        self.LabelDirectory.setText(self.__tr("Directory :"))
        self.radioButtonreadonly.setText(self.__tr("Read Only"))
        self.radioButtonReadWrite.setText(self.__tr("Read Write"))
        self.ButtonBrowse.setText(self.__tr("&Browse"))
        self.ButtonBrowse.setAccel(self.__tr("Alt+B"))
        self.lineDirectory.setText(QString.null)


    def ButtonBrowse_clicked(self):
        print "DialogProperties.ButtonBrowse_clicked(): Not implemented yet"

    def ButtonResolvUID_clicked(self):
        print "DialogProperties.ButtonResolvUID_clicked(): Not implemented yet"

    def ResolvGID_clicked(self):
        print "DialogProperties.ResolvGID_clicked(): Not implemented yet"

    def CheckAnonymous_clicked(self):
        print "DialogProperties.CheckAnonymous_clicked(): Not implemented yet"

    def CheckSpecifyUID_clicked(self):
        print "DialogProperties.CheckSpecifyUID_clicked(): Not implemented yet"

    def CheckSpecifyGID_clicked(self):
        print "DialogProperties.CheckSpecifyGID_clicked(): Not implemented yet"

    def radioButtonreadonly_clicked(self):
        print "DialogProperties.radioButtonreadonly_clicked(): Not implemented yet"

    def radioButtonReadWrite_clicked(self):
        print "DialogProperties.radioButtonReadWrite_clicked(): Not implemented yet"

    def buttonOk_clicked(self):
        print "DialogProperties.buttonOk_clicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DialogProperties",s,c)
