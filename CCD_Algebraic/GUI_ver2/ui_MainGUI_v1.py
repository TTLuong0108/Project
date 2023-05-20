# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainGUI_v1BDeFdh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 598)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSub{\n"
"	background-color: #15191d;\n"
"}\n"
"#leftMenuSub QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSub{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4 ,#popupNotificationSub{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#Header,#footer{\n"
"	background-color: #2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSub = QWidget(self.leftMenu)
        self.leftMenuSub.setObjectName(u"leftMenuSub")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSub)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSub)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u"../icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSub)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color:#1f232a;")
        icon1 = QIcon()
        icon1.addFile(u"../icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.connectBtn = QPushButton(self.frame_2)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u"../icons/link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.connectBtn.setIcon(icon2)
        self.connectBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.connectBtn)

        self.kinematicBtn = QPushButton(self.frame_2)
        self.kinematicBtn.setObjectName(u"kinematicBtn")
        self.kinematicBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u"../icons/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.kinematicBtn.setIcon(icon3)
        self.kinematicBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.kinematicBtn)

        self.trajectoryBtn = QPushButton(self.frame_2)
        self.trajectoryBtn.setObjectName(u"trajectoryBtn")
        self.trajectoryBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u"../icons/bookmark.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.trajectoryBtn.setIcon(icon4)
        self.trajectoryBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.trajectoryBtn)

        self.signalBtn = QPushButton(self.frame_2)
        self.signalBtn.setObjectName(u"signalBtn")
        self.signalBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u"../icons/trello.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.signalBtn.setIcon(icon5)
        self.signalBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.signalBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSub)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settingBtn = QPushButton(self.frame_3)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u"../icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon6)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingBtn)

        self.aboutBtn = QPushButton(self.frame_3)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u"../icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon7)
        self.aboutBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.aboutBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSub)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBody)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Header = QWidget(self.mainBody)
        self.Header.setObjectName(u"Header")
        self.horizontalLayout_5 = QHBoxLayout(self.Header)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.frame_5 = QFrame(self.Header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.lbl_DataStatus = QLabel(self.frame_5)
        self.lbl_DataStatus.setObjectName(u"lbl_DataStatus")
        self.lbl_DataStatus.setFont(font)
        self.lbl_DataStatus.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_7.addWidget(self.lbl_DataStatus)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.Header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.notificatioBtn = QPushButton(self.frame_6)
        self.notificatioBtn.setObjectName(u"notificatioBtn")
        icon8 = QIcon()
        icon8.addFile(u"../icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificatioBtn.setIcon(icon8)
        self.notificatioBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificatioBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.Header)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.MinimizeWinBtn = QPushButton(self.frame_7)
        self.MinimizeWinBtn.setObjectName(u"MinimizeWinBtn")
        icon9 = QIcon()
        icon9.addFile(u"../icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeWinBtn.setIcon(icon9)
        self.MinimizeWinBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.MinimizeWinBtn)

        self.RestoreWinBtn = QPushButton(self.frame_7)
        self.RestoreWinBtn.setObjectName(u"RestoreWinBtn")
        icon10 = QIcon()
        icon10.addFile(u"../icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RestoreWinBtn.setIcon(icon10)
        self.RestoreWinBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.RestoreWinBtn)

        self.CloseWinBtn = QPushButton(self.frame_7)
        self.CloseWinBtn.setObjectName(u"CloseWinBtn")
        icon11 = QIcon()
        icon11.addFile(u"../icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseWinBtn.setIcon(icon11)
        self.CloseWinBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.CloseWinBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.Header, 0, Qt.AlignTop)

        self.Body = QWidget(self.mainBody)
        self.Body.setObjectName(u"Body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.Body)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QCustomStackedWidget(self.Body)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.label_2 = QLabel(self.pageHome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 30, 651, 19))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_54 = QLabel(self.pageHome)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(120, 210, 521, 19))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy3)
        self.label_54.setFont(font)
        self.stackedWidget_2.addWidget(self.pageHome)
        self.pageConnected = QWidget()
        self.pageConnected.setObjectName(u"pageConnected")
        self.verticalLayout_5 = QVBoxLayout(self.pageConnected)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ConnectMid = QWidget(self.pageConnected)
        self.ConnectMid.setObjectName(u"ConnectMid")
        sizePolicy.setHeightForWidth(self.ConnectMid.sizePolicy().hasHeightForWidth())
        self.ConnectMid.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.ConnectMid)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.ConnectMid)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 100))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_5, 0, Qt.AlignRight)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QSize(200, 100))
        self.label_12.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_12)


        self.horizontalLayout_3.addWidget(self.widget, 0, Qt.AlignRight)

        self.widget_2 = QWidget(self.ConnectMid)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setSpacing(22)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cbbCom = QComboBox(self.widget_2)
        self.cbbCom.setObjectName(u"cbbCom")
        sizePolicy.setHeightForWidth(self.cbbCom.sizePolicy().hasHeightForWidth())
        self.cbbCom.setSizePolicy(sizePolicy)
        self.cbbCom.setMaximumSize(QSize(250, 50))
        self.cbbCom.setFont(font2)
        self.cbbCom.setStyleSheet(u"background-color:rgb(0, 85, 0);")

        self.verticalLayout_7.addWidget(self.cbbCom)

        self.cbbBaudrate = QComboBox(self.widget_2)
        self.cbbBaudrate.addItem("")
        self.cbbBaudrate.addItem("")
        self.cbbBaudrate.setObjectName(u"cbbBaudrate")
        sizePolicy.setHeightForWidth(self.cbbBaudrate.sizePolicy().hasHeightForWidth())
        self.cbbBaudrate.setSizePolicy(sizePolicy)
        self.cbbBaudrate.setMaximumSize(QSize(250, 50))
        self.cbbBaudrate.setFont(font2)
        self.cbbBaudrate.setStyleSheet(u"background-color:rgb(0, 85, 0);")

        self.verticalLayout_7.addWidget(self.cbbBaudrate)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout_5.addWidget(self.ConnectMid)

        self.ConnectBottom = QWidget(self.pageConnected)
        self.ConnectBottom.setObjectName(u"ConnectBottom")
        self.ConnectBottom.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.ConnectBottom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.ConnectBottom)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_18 = QVBoxLayout(self.widget_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_13 = QLabel(self.widget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(400, 100))
        self.label_13.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_13, 0, Qt.AlignRight)


        self.horizontalLayout_11.addWidget(self.widget_5, 0, Qt.AlignRight)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(400, 40))
        self.verticalLayout_19 = QVBoxLayout(self.widget_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.checkBox = QCheckBox(self.widget_6)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy4)
        self.checkBox.setFont(font2)
        self.checkBox.setIconSize(QSize(24, 24))
        self.checkBox.setTristate(False)

        self.verticalLayout_19.addWidget(self.checkBox)


        self.horizontalLayout_11.addWidget(self.widget_6)


        self.verticalLayout_8.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.widget_4 = QWidget(self.ConnectBottom)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.widget_4.setFont(font2)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.UpdatePortBtn = QPushButton(self.widget_4)
        self.UpdatePortBtn.setObjectName(u"UpdatePortBtn")
        self.UpdatePortBtn.setMaximumSize(QSize(150, 50))
        self.UpdatePortBtn.setFont(font)
        self.UpdatePortBtn.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout_15.addWidget(self.UpdatePortBtn)

        self.ConnectedBtn = QPushButton(self.widget_4)
        self.ConnectedBtn.setObjectName(u"ConnectedBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ConnectedBtn.sizePolicy().hasHeightForWidth())
        self.ConnectedBtn.setSizePolicy(sizePolicy5)
        self.ConnectedBtn.setMaximumSize(QSize(150, 50))
        self.ConnectedBtn.setFont(font)
        self.ConnectedBtn.setStyleSheet(u"\n"
"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_15.addWidget(self.ConnectedBtn)


        self.verticalLayout_8.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.ConnectBottom)

        self.stackedWidget_2.addWidget(self.pageConnected)
        self.pageKinematic = QWidget()
        self.pageKinematic.setObjectName(u"pageKinematic")
        self.verticalLayout_13 = QVBoxLayout(self.pageKinematic)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_13 = QFrame(self.pageKinematic)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_13)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pageKinematic_top = QFrame(self.frame_13)
        self.pageKinematic_top.setObjectName(u"pageKinematic_top")
        self.pageKinematic_top.setFrameShape(QFrame.StyledPanel)
        self.pageKinematic_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.pageKinematic_top)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_6 = QLabel(self.pageKinematic_top)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_24.addWidget(self.label_6)


        self.verticalLayout_21.addWidget(self.pageKinematic_top, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pageKinematic_body = QFrame(self.frame_13)
        self.pageKinematic_body.setObjectName(u"pageKinematic_body")
        self.pageKinematic_body.setFrameShape(QFrame.StyledPanel)
        self.pageKinematic_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.pageKinematic_body)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, -1)
        self.frame_15 = QFrame(self.pageKinematic_body)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_19)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_19)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(60, 30))
        self.label_24.setFont(font)

        self.verticalLayout_26.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_19)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(60, 30))
        self.label_25.setFont(font)

        self.verticalLayout_26.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_19)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(60, 30))
        self.label_26.setFont(font)

        self.verticalLayout_26.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_19)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(60, 30))
        self.label_27.setFont(font)

        self.verticalLayout_26.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(60, 30))
        self.label_28.setFont(font)

        self.verticalLayout_26.addWidget(self.label_28)

        self.label_30 = QLabel(self.frame_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(60, 30))
        self.label_30.setFont(font)

        self.verticalLayout_26.addWidget(self.label_30)


        self.horizontalLayout_26.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_20)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.slider_t1 = QSlider(self.frame_20)
        self.slider_t1.setObjectName(u"slider_t1")
        self.slider_t1.setMaximumSize(QSize(300, 30))
        self.slider_t1.setMinimum(-4500)
        self.slider_t1.setMaximum(4500)
        self.slider_t1.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t1)

        self.slider_t2 = QSlider(self.frame_20)
        self.slider_t2.setObjectName(u"slider_t2")
        self.slider_t2.setMaximumSize(QSize(300, 30))
        self.slider_t2.setMinimum(-3000)
        self.slider_t2.setMaximum(4500)
        self.slider_t2.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t2)

        self.slider_t3 = QSlider(self.frame_20)
        self.slider_t3.setObjectName(u"slider_t3")
        self.slider_t3.setMaximumSize(QSize(300, 30))
        self.slider_t3.setMinimum(-4500)
        self.slider_t3.setMaximum(4500)
        self.slider_t3.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t3)

        self.slider_t4 = QSlider(self.frame_20)
        self.slider_t4.setObjectName(u"slider_t4")
        self.slider_t4.setMaximumSize(QSize(300, 30))
        self.slider_t4.setMinimum(-3000)
        self.slider_t4.setMaximum(4500)
        self.slider_t4.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t4)

        self.slider_t5 = QSlider(self.frame_20)
        self.slider_t5.setObjectName(u"slider_t5")
        self.slider_t5.setMaximumSize(QSize(300, 30))
        self.slider_t5.setMinimum(-4500)
        self.slider_t5.setMaximum(4500)
        self.slider_t5.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t5)

        self.slider_t6 = QSlider(self.frame_20)
        self.slider_t6.setObjectName(u"slider_t6")
        self.slider_t6.setMaximumSize(QSize(300, 30))
        self.slider_t6.setMinimum(-4500)
        self.slider_t6.setMaximum(4500)
        self.slider_t6.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t6)


        self.horizontalLayout_26.addWidget(self.frame_20)


        self.horizontalLayout_24.addWidget(self.frame_15)

        self.frame_18 = QFrame(self.pageKinematic_body)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_28.setSpacing(30)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_17)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(30, 0, 0, 0)
        self.textEdit_FK_t1 = QTextEdit(self.frame_17)
        self.textEdit_FK_t1.setObjectName(u"textEdit_FK_t1")
        self.textEdit_FK_t1.setMaximumSize(QSize(80, 30))
        self.textEdit_FK_t1.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t1)

        self.textEdit_FK_t2 = QTextEdit(self.frame_17)
        self.textEdit_FK_t2.setObjectName(u"textEdit_FK_t2")
        self.textEdit_FK_t2.setMaximumSize(QSize(80, 30))
        self.textEdit_FK_t2.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t2)

        self.textEdit_FK_t3 = QTextEdit(self.frame_17)
        self.textEdit_FK_t3.setObjectName(u"textEdit_FK_t3")
        self.textEdit_FK_t3.setMaximumSize(QSize(80, 30))
        self.textEdit_FK_t3.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t3)

        self.textEdit_FK_t4 = QTextEdit(self.frame_17)
        self.textEdit_FK_t4.setObjectName(u"textEdit_FK_t4")
        self.textEdit_FK_t4.setMaximumSize(QSize(80, 30))
        self.textEdit_FK_t4.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t4)

        self.textEdit_FK_t5 = QTextEdit(self.frame_17)
        self.textEdit_FK_t5.setObjectName(u"textEdit_FK_t5")
        self.textEdit_FK_t5.setMaximumSize(QSize(80, 30))
        self.textEdit_FK_t5.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t5)

        self.textEdit_FK_t6 = QTextEdit(self.frame_17)
        self.textEdit_FK_t6.setObjectName(u"textEdit_FK_t6")
        self.textEdit_FK_t6.setMaximumSize(QSize(80, 30))
        self.textEdit_FK_t6.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t6)


        self.horizontalLayout_28.addWidget(self.frame_17)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_21)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_21)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.verticalLayout_25.addWidget(self.label_29)

        self.label_31 = QLabel(self.frame_21)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.verticalLayout_25.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_21)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.verticalLayout_25.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_21)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.verticalLayout_25.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_21)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)

        self.verticalLayout_25.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_21)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.verticalLayout_25.addWidget(self.label_35)


        self.horizontalLayout_28.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_18)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_22)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.FK_Px = QTextEdit(self.frame_22)
        self.FK_Px.setObjectName(u"FK_Px")
        self.FK_Px.setMaximumSize(QSize(100, 30))
        self.FK_Px.setFont(font)

        self.verticalLayout_29.addWidget(self.FK_Px)

        self.FK_Py = QTextEdit(self.frame_22)
        self.FK_Py.setObjectName(u"FK_Py")
        self.FK_Py.setMaximumSize(QSize(100, 30))
        self.FK_Py.setFont(font)

        self.verticalLayout_29.addWidget(self.FK_Py)

        self.FK_Pz = QTextEdit(self.frame_22)
        self.FK_Pz.setObjectName(u"FK_Pz")
        self.FK_Pz.setMaximumSize(QSize(100, 30))
        self.FK_Pz.setFont(font)

        self.verticalLayout_29.addWidget(self.FK_Pz)

        self.alpha = QTextEdit(self.frame_22)
        self.alpha.setObjectName(u"alpha")
        self.alpha.setMaximumSize(QSize(100, 30))
        self.alpha.setFont(font)

        self.verticalLayout_29.addWidget(self.alpha)

        self.beta = QTextEdit(self.frame_22)
        self.beta.setObjectName(u"beta")
        self.beta.setMaximumSize(QSize(100, 30))
        self.beta.setFont(font)

        self.verticalLayout_29.addWidget(self.beta)

        self.gama = QTextEdit(self.frame_22)
        self.gama.setObjectName(u"gama")
        self.gama.setMaximumSize(QSize(100, 30))
        self.gama.setFont(font)

        self.verticalLayout_29.addWidget(self.gama)


        self.horizontalLayout_28.addWidget(self.frame_22)


        self.horizontalLayout_24.addWidget(self.frame_18)


        self.verticalLayout_21.addWidget(self.pageKinematic_body)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.pageKinematic)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Solve_FK = QPushButton(self.frame_14)
        self.Solve_FK.setObjectName(u"Solve_FK")
        self.Solve_FK.setMaximumSize(QSize(200, 40))
        self.Solve_FK.setFont(font)
        self.Solve_FK.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_27.addWidget(self.Solve_FK)

        self.Solve_IK = QPushButton(self.frame_14)
        self.Solve_IK.setObjectName(u"Solve_IK")
        self.Solve_IK.setMaximumSize(QSize(200, 40))
        self.Solve_IK.setFont(font)
        self.Solve_IK.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_27.addWidget(self.Solve_IK)


        self.verticalLayout_13.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.pageKinematic)
        self.pageTrajectory = QWidget()
        self.pageTrajectory.setObjectName(u"pageTrajectory")
        self.verticalLayout_30 = QVBoxLayout(self.pageTrajectory)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.widget_61 = QWidget(self.pageTrajectory)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_47 = QVBoxLayout(self.widget_61)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.widget_62 = QWidget(self.widget_61)
        self.widget_62.setObjectName(u"widget_62")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_7 = QLabel(self.widget_62)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_61.addWidget(self.label_7)

        self.label_14 = QLabel(self.widget_62)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_61.addWidget(self.label_14)

        self.Stop_draw = QPushButton(self.widget_62)
        self.Stop_draw.setObjectName(u"Stop_draw")
        sizePolicy4.setHeightForWidth(self.Stop_draw.sizePolicy().hasHeightForWidth())
        self.Stop_draw.setSizePolicy(sizePolicy4)
        self.Stop_draw.setFont(font)
        self.Stop_draw.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_61.addWidget(self.Stop_draw)


        self.verticalLayout_47.addWidget(self.widget_62)

        self.widget_63 = QWidget(self.widget_61)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.Lines = QPushButton(self.widget_63)
        self.Lines.setObjectName(u"Lines")
        sizePolicy4.setHeightForWidth(self.Lines.sizePolicy().hasHeightForWidth())
        self.Lines.setSizePolicy(sizePolicy4)
        self.Lines.setFont(font)
        self.Lines.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_60.addWidget(self.Lines)

        self.Triangles = QPushButton(self.widget_63)
        self.Triangles.setObjectName(u"Triangles")
        sizePolicy4.setHeightForWidth(self.Triangles.sizePolicy().hasHeightForWidth())
        self.Triangles.setSizePolicy(sizePolicy4)
        self.Triangles.setFont(font)
        self.Triangles.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_60.addWidget(self.Triangles)

        self.Circles = QPushButton(self.widget_63)
        self.Circles.setObjectName(u"Circles")
        sizePolicy4.setHeightForWidth(self.Circles.sizePolicy().hasHeightForWidth())
        self.Circles.setSizePolicy(sizePolicy4)
        self.Circles.setFont(font)
        self.Circles.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_60.addWidget(self.Circles)


        self.verticalLayout_47.addWidget(self.widget_63)


        self.verticalLayout_30.addWidget(self.widget_61)

        self.widget_60 = QWidget(self.pageTrajectory)
        self.widget_60.setObjectName(u"widget_60")
        sizePolicy.setHeightForWidth(self.widget_60.sizePolicy().hasHeightForWidth())
        self.widget_60.setSizePolicy(sizePolicy)
        self.widget_60.setMaximumSize(QSize(16777215, 600))
        self.horizontalLayout_51 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.XOY_demension = QVBoxLayout()
        self.XOY_demension.setObjectName(u"XOY_demension")

        self.horizontalLayout_51.addLayout(self.XOY_demension)

        self.YOZ_demension = QVBoxLayout()
        self.YOZ_demension.setObjectName(u"YOZ_demension")

        self.horizontalLayout_51.addLayout(self.YOZ_demension)

        self.XOZ_demension = QVBoxLayout()
        self.XOZ_demension.setObjectName(u"XOZ_demension")

        self.horizontalLayout_51.addLayout(self.XOZ_demension)


        self.verticalLayout_30.addWidget(self.widget_60)

        self.stackedWidget_2.addWidget(self.pageTrajectory)
        self.pageSignal = QWidget()
        self.pageSignal.setObjectName(u"pageSignal")
        self.verticalLayout_15 = QVBoxLayout(self.pageSignal)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_7 = QWidget(self.pageSignal)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.widget_7.setMaximumSize(QSize(16777215, 55))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.SignalOutputBtn = QPushButton(self.widget_7)
        self.SignalOutputBtn.setObjectName(u"SignalOutputBtn")
        self.SignalOutputBtn.setMaximumSize(QSize(16777215, 55))
        self.SignalOutputBtn.setFont(font)
        self.SignalOutputBtn.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_12.addWidget(self.SignalOutputBtn)

        self.SignalErrorBtn = QPushButton(self.widget_7)
        self.SignalErrorBtn.setObjectName(u"SignalErrorBtn")
        self.SignalErrorBtn.setMaximumSize(QSize(16777215, 55))
        self.SignalErrorBtn.setFont(font)
        self.SignalErrorBtn.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_12.addWidget(self.SignalErrorBtn)

        self.PositionOutputBtn = QPushButton(self.widget_7)
        self.PositionOutputBtn.setObjectName(u"PositionOutputBtn")
        self.PositionOutputBtn.setMaximumSize(QSize(16777215, 55))
        self.PositionOutputBtn.setFont(font)
        self.PositionOutputBtn.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_12.addWidget(self.PositionOutputBtn)

        self.PositionErrorBtn = QPushButton(self.widget_7)
        self.PositionErrorBtn.setObjectName(u"PositionErrorBtn")
        self.PositionErrorBtn.setMaximumSize(QSize(16777215, 55))
        self.PositionErrorBtn.setFont(font)
        self.PositionErrorBtn.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_12.addWidget(self.PositionErrorBtn)


        self.verticalLayout_15.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.pageSignal)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMaximumSize(QSize(16777215, 550))
        self.verticalLayout_20 = QVBoxLayout(self.widget_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.stackedWidget = QStackedWidget(self.widget_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.SignalOutput = QWidget()
        self.SignalOutput.setObjectName(u"SignalOutput")
        self.verticalLayout_23 = QVBoxLayout(self.SignalOutput)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_9 = QWidget(self.SignalOutput)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Theta1Output = QVBoxLayout()
        self.Theta1Output.setObjectName(u"Theta1Output")

        self.horizontalLayout_14.addLayout(self.Theta1Output)

        self.Theta2Output = QVBoxLayout()
        self.Theta2Output.setObjectName(u"Theta2Output")

        self.horizontalLayout_14.addLayout(self.Theta2Output)

        self.Theta3Output = QVBoxLayout()
        self.Theta3Output.setObjectName(u"Theta3Output")

        self.horizontalLayout_14.addLayout(self.Theta3Output)


        self.verticalLayout_23.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.SignalOutput)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Theta4Output = QVBoxLayout()
        self.Theta4Output.setObjectName(u"Theta4Output")

        self.horizontalLayout_13.addLayout(self.Theta4Output)

        self.Theta5Output = QVBoxLayout()
        self.Theta5Output.setObjectName(u"Theta5Output")

        self.horizontalLayout_13.addLayout(self.Theta5Output)

        self.Theta6Output = QVBoxLayout()
        self.Theta6Output.setObjectName(u"Theta6Output")

        self.horizontalLayout_13.addLayout(self.Theta6Output)


        self.verticalLayout_23.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.SignalOutput)
        self.SignalError = QWidget()
        self.SignalError.setObjectName(u"SignalError")
        self.verticalLayout_14 = QVBoxLayout(self.SignalError)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_11 = QWidget(self.SignalError)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Theta1Error = QVBoxLayout()
        self.Theta1Error.setObjectName(u"Theta1Error")

        self.horizontalLayout_16.addLayout(self.Theta1Error)

        self.Theta2Error = QVBoxLayout()
        self.Theta2Error.setObjectName(u"Theta2Error")

        self.horizontalLayout_16.addLayout(self.Theta2Error)

        self.Theta3Error = QVBoxLayout()
        self.Theta3Error.setObjectName(u"Theta3Error")

        self.horizontalLayout_16.addLayout(self.Theta3Error)


        self.verticalLayout_14.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.SignalError)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.Theta4Error = QVBoxLayout()
        self.Theta4Error.setObjectName(u"Theta4Error")

        self.horizontalLayout_31.addLayout(self.Theta4Error)

        self.Theta5Error = QVBoxLayout()
        self.Theta5Error.setObjectName(u"Theta5Error")

        self.horizontalLayout_31.addLayout(self.Theta5Error)

        self.Theta6Error = QVBoxLayout()
        self.Theta6Error.setObjectName(u"Theta6Error")

        self.horizontalLayout_31.addLayout(self.Theta6Error)


        self.verticalLayout_14.addWidget(self.widget_12)

        self.stackedWidget.addWidget(self.SignalError)
        self.PositionOutput = QWidget()
        self.PositionOutput.setObjectName(u"PositionOutput")
        self.verticalLayout_22 = QVBoxLayout(self.PositionOutput)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_56 = QWidget(self.PositionOutput)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.XOuput = QVBoxLayout()
        self.XOuput.setObjectName(u"XOuput")

        self.horizontalLayout_47.addLayout(self.XOuput)

        self.YOuput = QVBoxLayout()
        self.YOuput.setObjectName(u"YOuput")

        self.horizontalLayout_47.addLayout(self.YOuput)

        self.ZOuput = QVBoxLayout()
        self.ZOuput.setObjectName(u"ZOuput")

        self.horizontalLayout_47.addLayout(self.ZOuput)


        self.verticalLayout_22.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.PositionOutput)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.alphaOuput = QVBoxLayout()
        self.alphaOuput.setObjectName(u"alphaOuput")

        self.horizontalLayout_48.addLayout(self.alphaOuput)

        self.betaOuput = QVBoxLayout()
        self.betaOuput.setObjectName(u"betaOuput")

        self.horizontalLayout_48.addLayout(self.betaOuput)

        self.gamaOutput = QVBoxLayout()
        self.gamaOutput.setObjectName(u"gamaOutput")

        self.horizontalLayout_48.addLayout(self.gamaOutput)


        self.verticalLayout_22.addWidget(self.widget_57)

        self.stackedWidget.addWidget(self.PositionOutput)
        self.PositionError = QWidget()
        self.PositionError.setObjectName(u"PositionError")
        self.verticalLayout_12 = QVBoxLayout(self.PositionError)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_58 = QWidget(self.PositionError)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.XError = QVBoxLayout()
        self.XError.setObjectName(u"XError")

        self.horizontalLayout_49.addLayout(self.XError)

        self.YError = QVBoxLayout()
        self.YError.setObjectName(u"YError")

        self.horizontalLayout_49.addLayout(self.YError)

        self.ZError = QVBoxLayout()
        self.ZError.setObjectName(u"ZError")

        self.horizontalLayout_49.addLayout(self.ZError)


        self.verticalLayout_12.addWidget(self.widget_58)

        self.widget_59 = QWidget(self.PositionError)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.alphaError = QVBoxLayout()
        self.alphaError.setObjectName(u"alphaError")

        self.horizontalLayout_50.addLayout(self.alphaError)

        self.betaError = QVBoxLayout()
        self.betaError.setObjectName(u"betaError")

        self.horizontalLayout_50.addLayout(self.betaError)

        self.gamaError = QVBoxLayout()
        self.gamaError.setObjectName(u"gamaError")

        self.horizontalLayout_50.addLayout(self.gamaError)


        self.verticalLayout_12.addWidget(self.widget_59)

        self.stackedWidget.addWidget(self.PositionError)

        self.verticalLayout_20.addWidget(self.stackedWidget)


        self.verticalLayout_15.addWidget(self.widget_8)

        self.stackedWidget_2.addWidget(self.pageSignal)
        self.pageSetting = QWidget()
        self.pageSetting.setObjectName(u"pageSetting")
        self.horizontalLayout_17 = QHBoxLayout(self.pageSetting)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.Setting_Theta_Init = QWidget(self.pageSetting)
        self.Setting_Theta_Init.setObjectName(u"Setting_Theta_Init")
        self.verticalLayout_34 = QVBoxLayout(self.Setting_Theta_Init)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.Setting_Theta_Init)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.verticalLayout_35 = QVBoxLayout(self.widget_22)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_22)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_35.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.widget_22, 0, Qt.AlignTop)

        self.widget_23 = QWidget(self.Setting_Theta_Init)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy2.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy2)
        self.widget_23.setStyleSheet(u"background-color: rgb(109, 109, 109);")
        self.verticalLayout_43 = QVBoxLayout(self.widget_23)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.widget_27 = QWidget(self.widget_23)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_20 = QLabel(self.widget_27)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(70, 30))
        self.label_20.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_20)

        self.Setting_Theta1_init = QTextEdit(self.widget_27)
        self.Setting_Theta1_init.setObjectName(u"Setting_Theta1_init")
        self.Setting_Theta1_init.setMaximumSize(QSize(70, 30))
        self.Setting_Theta1_init.setFont(font)
        self.Setting_Theta1_init.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_21.addWidget(self.Setting_Theta1_init)


        self.verticalLayout_43.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_23)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_21 = QLabel(self.widget_28)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(70, 30))
        self.label_21.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_21)

        self.Setting_Theta2_init = QTextEdit(self.widget_28)
        self.Setting_Theta2_init.setObjectName(u"Setting_Theta2_init")
        self.Setting_Theta2_init.setMaximumSize(QSize(70, 30))
        self.Setting_Theta2_init.setFont(font)
        self.Setting_Theta2_init.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_22.addWidget(self.Setting_Theta2_init)


        self.verticalLayout_43.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_23)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_22 = QLabel(self.widget_29)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(70, 30))
        self.label_22.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_22)

        self.Setting_Theta3_init = QTextEdit(self.widget_29)
        self.Setting_Theta3_init.setObjectName(u"Setting_Theta3_init")
        self.Setting_Theta3_init.setMaximumSize(QSize(70, 30))
        self.Setting_Theta3_init.setFont(font)
        self.Setting_Theta3_init.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_23.addWidget(self.Setting_Theta3_init)


        self.verticalLayout_43.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_23)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_23 = QLabel(self.widget_30)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(70, 30))
        self.label_23.setFont(font)

        self.horizontalLayout_25.addWidget(self.label_23)

        self.Setting_Theta4_init = QTextEdit(self.widget_30)
        self.Setting_Theta4_init.setObjectName(u"Setting_Theta4_init")
        self.Setting_Theta4_init.setMaximumSize(QSize(70, 30))
        self.Setting_Theta4_init.setFont(font)
        self.Setting_Theta4_init.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_25.addWidget(self.Setting_Theta4_init)


        self.verticalLayout_43.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.widget_23)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_36 = QLabel(self.widget_31)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(70, 30))
        self.label_36.setFont(font)

        self.horizontalLayout_29.addWidget(self.label_36)

        self.Setting_Theta5_init = QTextEdit(self.widget_31)
        self.Setting_Theta5_init.setObjectName(u"Setting_Theta5_init")
        self.Setting_Theta5_init.setMaximumSize(QSize(70, 30))
        self.Setting_Theta5_init.setFont(font)
        self.Setting_Theta5_init.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_29.addWidget(self.Setting_Theta5_init)


        self.verticalLayout_43.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.widget_23)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_37 = QLabel(self.widget_32)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(70, 30))
        self.label_37.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_37)

        self.Setting_Theta6_init = QTextEdit(self.widget_32)
        self.Setting_Theta6_init.setObjectName(u"Setting_Theta6_init")
        self.Setting_Theta6_init.setMaximumSize(QSize(70, 30))
        self.Setting_Theta6_init.setFont(font)
        self.Setting_Theta6_init.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_30.addWidget(self.Setting_Theta6_init)


        self.verticalLayout_43.addWidget(self.widget_32)


        self.verticalLayout_34.addWidget(self.widget_23)


        self.horizontalLayout_17.addWidget(self.Setting_Theta_Init)

        self.Setting_Home = QWidget(self.pageSetting)
        self.Setting_Home.setObjectName(u"Setting_Home")
        self.verticalLayout_31 = QVBoxLayout(self.Setting_Home)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.Setting_Home)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_32 = QVBoxLayout(self.widget_13)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout_32.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_31.addWidget(self.widget_13, 0, Qt.AlignTop)

        self.widget_14 = QWidget(self.Setting_Home)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy2.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy2)
        self.verticalLayout_33 = QVBoxLayout(self.widget_14)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(16777215, 16777215))
        self.widget_15.setStyleSheet(u"background-color: rgb(109, 109, 109);")
        self.verticalLayout_42 = QVBoxLayout(self.widget_15)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.widget_24 = QWidget(self.widget_15)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_24)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(70, 30))
        self.label_17.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_17, 0, Qt.AlignRight)

        self.Setting_Px_Home = QTextEdit(self.widget_24)
        self.Setting_Px_Home.setObjectName(u"Setting_Px_Home")
        self.Setting_Px_Home.setMaximumSize(QSize(70, 30))
        self.Setting_Px_Home.setFont(font)
        self.Setting_Px_Home.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_18.addWidget(self.Setting_Px_Home)


        self.verticalLayout_42.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_15)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_25)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(70, 30))
        self.label_18.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_18, 0, Qt.AlignRight)

        self.Setting_Py_Home = QTextEdit(self.widget_25)
        self.Setting_Py_Home.setObjectName(u"Setting_Py_Home")
        self.Setting_Py_Home.setMaximumSize(QSize(70, 30))
        self.Setting_Py_Home.setFont(font)
        self.Setting_Py_Home.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_19.addWidget(self.Setting_Py_Home)


        self.verticalLayout_42.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.widget_15)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_26)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(70, 30))
        self.label_19.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_19, 0, Qt.AlignRight)

        self.Setting_Pz_Home = QTextEdit(self.widget_26)
        self.Setting_Pz_Home.setObjectName(u"Setting_Pz_Home")
        self.Setting_Pz_Home.setMaximumSize(QSize(70, 30))
        self.Setting_Pz_Home.setFont(font)
        self.Setting_Pz_Home.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_20.addWidget(self.Setting_Pz_Home)


        self.verticalLayout_42.addWidget(self.widget_26)

        self.widget_48 = QWidget(self.widget_15)
        self.widget_48.setObjectName(u"widget_48")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.widget_48)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(70, 30))
        self.label_59.setFont(font)

        self.horizontalLayout_52.addWidget(self.label_59, 0, Qt.AlignRight)

        self.Setting_L1 = QTextEdit(self.widget_48)
        self.Setting_L1.setObjectName(u"Setting_L1")
        self.Setting_L1.setMaximumSize(QSize(70, 30))
        self.Setting_L1.setFont(font)
        self.Setting_L1.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_52.addWidget(self.Setting_L1)


        self.verticalLayout_42.addWidget(self.widget_48)

        self.widget_50 = QWidget(self.widget_15)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.widget_50)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(70, 30))
        self.label_61.setFont(font)

        self.horizontalLayout_54.addWidget(self.label_61, 0, Qt.AlignRight)

        self.Setting_L2 = QTextEdit(self.widget_50)
        self.Setting_L2.setObjectName(u"Setting_L2")
        self.Setting_L2.setMaximumSize(QSize(70, 30))
        self.Setting_L2.setFont(font)
        self.Setting_L2.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_54.addWidget(self.Setting_L2)


        self.verticalLayout_42.addWidget(self.widget_50)

        self.widget_51 = QWidget(self.widget_15)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.widget_51)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(70, 30))
        self.label_62.setFont(font)

        self.horizontalLayout_55.addWidget(self.label_62, 0, Qt.AlignRight)

        self.Setting_L3 = QTextEdit(self.widget_51)
        self.Setting_L3.setObjectName(u"Setting_L3")
        self.Setting_L3.setMaximumSize(QSize(70, 30))
        self.Setting_L3.setFont(font)
        self.Setting_L3.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_55.addWidget(self.Setting_L3)


        self.verticalLayout_42.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.widget_15)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.widget_52)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(70, 30))
        self.label_63.setFont(font)

        self.horizontalLayout_56.addWidget(self.label_63, 0, Qt.AlignRight)

        self.Setting_L4 = QTextEdit(self.widget_52)
        self.Setting_L4.setObjectName(u"Setting_L4")
        self.Setting_L4.setMaximumSize(QSize(70, 30))
        self.Setting_L4.setFont(font)
        self.Setting_L4.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_56.addWidget(self.Setting_L4)


        self.verticalLayout_42.addWidget(self.widget_52)


        self.verticalLayout_33.addWidget(self.widget_15)


        self.verticalLayout_31.addWidget(self.widget_14)


        self.horizontalLayout_17.addWidget(self.Setting_Home)

        self.Setting_Lines = QWidget(self.pageSetting)
        self.Setting_Lines.setObjectName(u"Setting_Lines")
        self.verticalLayout_36 = QVBoxLayout(self.Setting_Lines)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.Setting_Lines)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_37 = QVBoxLayout(self.widget_16)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout_37.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_36.addWidget(self.widget_16, 0, Qt.AlignTop)

        self.widget_17 = QWidget(self.Setting_Lines)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy2.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy2)
        self.widget_17.setStyleSheet(u"background-color: rgb(109, 109, 109);")
        self.verticalLayout_44 = QVBoxLayout(self.widget_17)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.widget_33 = QWidget(self.widget_17)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_39 = QLabel(self.widget_33)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(70, 30))
        self.label_39.setFont(font)

        self.horizontalLayout_32.addWidget(self.label_39)

        self.Setting_Px1_Line = QTextEdit(self.widget_33)
        self.Setting_Px1_Line.setObjectName(u"Setting_Px1_Line")
        self.Setting_Px1_Line.setMaximumSize(QSize(70, 30))
        self.Setting_Px1_Line.setFont(font)
        self.Setting_Px1_Line.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_32.addWidget(self.Setting_Px1_Line)


        self.verticalLayout_44.addWidget(self.widget_33)

        self.widget_35 = QWidget(self.widget_17)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_40 = QLabel(self.widget_35)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(70, 30))
        self.label_40.setFont(font)

        self.horizontalLayout_33.addWidget(self.label_40)

        self.Setting_Py1_Line = QTextEdit(self.widget_35)
        self.Setting_Py1_Line.setObjectName(u"Setting_Py1_Line")
        self.Setting_Py1_Line.setMaximumSize(QSize(70, 30))
        self.Setting_Py1_Line.setFont(font)
        self.Setting_Py1_Line.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_33.addWidget(self.Setting_Py1_Line)


        self.verticalLayout_44.addWidget(self.widget_35)

        self.widget_34 = QWidget(self.widget_17)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_41 = QLabel(self.widget_34)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(70, 30))
        self.label_41.setFont(font)

        self.horizontalLayout_34.addWidget(self.label_41)

        self.Setting_Pz1_Line = QTextEdit(self.widget_34)
        self.Setting_Pz1_Line.setObjectName(u"Setting_Pz1_Line")
        self.Setting_Pz1_Line.setMaximumSize(QSize(70, 30))
        self.Setting_Pz1_Line.setFont(font)
        self.Setting_Pz1_Line.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_34.addWidget(self.Setting_Pz1_Line)


        self.verticalLayout_44.addWidget(self.widget_34)

        self.widget_36 = QWidget(self.widget_17)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_42 = QLabel(self.widget_36)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(70, 30))
        self.label_42.setFont(font)

        self.horizontalLayout_35.addWidget(self.label_42)

        self.Setting_Px2_Line = QTextEdit(self.widget_36)
        self.Setting_Px2_Line.setObjectName(u"Setting_Px2_Line")
        self.Setting_Px2_Line.setMaximumSize(QSize(70, 30))
        self.Setting_Px2_Line.setFont(font)
        self.Setting_Px2_Line.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_35.addWidget(self.Setting_Px2_Line)


        self.verticalLayout_44.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.widget_17)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_43 = QLabel(self.widget_37)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(70, 30))
        self.label_43.setFont(font)

        self.horizontalLayout_36.addWidget(self.label_43)

        self.Setting_Py2_Line = QTextEdit(self.widget_37)
        self.Setting_Py2_Line.setObjectName(u"Setting_Py2_Line")
        self.Setting_Py2_Line.setMaximumSize(QSize(70, 30))
        self.Setting_Py2_Line.setFont(font)
        self.Setting_Py2_Line.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_36.addWidget(self.Setting_Py2_Line)


        self.verticalLayout_44.addWidget(self.widget_37)

        self.widget_38 = QWidget(self.widget_17)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_44 = QLabel(self.widget_38)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(70, 30))
        self.label_44.setFont(font)

        self.horizontalLayout_37.addWidget(self.label_44)

        self.Setting_Pz2_Line = QTextEdit(self.widget_38)
        self.Setting_Pz2_Line.setObjectName(u"Setting_Pz2_Line")
        self.Setting_Pz2_Line.setMaximumSize(QSize(70, 30))
        self.Setting_Pz2_Line.setFont(font)
        self.Setting_Pz2_Line.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_37.addWidget(self.Setting_Pz2_Line)


        self.verticalLayout_44.addWidget(self.widget_38)


        self.verticalLayout_36.addWidget(self.widget_17)


        self.horizontalLayout_17.addWidget(self.Setting_Lines)

        self.Setting_Triangle = QWidget(self.pageSetting)
        self.Setting_Triangle.setObjectName(u"Setting_Triangle")
        self.verticalLayout_38 = QVBoxLayout(self.Setting_Triangle)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.Setting_Triangle)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_39 = QVBoxLayout(self.widget_18)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout_39.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.widget_18, 0, Qt.AlignTop)

        self.widget_19 = QWidget(self.Setting_Triangle)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy2.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy2)
        self.widget_19.setStyleSheet(u"background-color: rgb(109, 109, 109);")
        self.verticalLayout_45 = QVBoxLayout(self.widget_19)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.widget_39 = QWidget(self.widget_19)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.widget_39)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(50, 30))
        self.label_45.setFont(font)

        self.horizontalLayout_38.addWidget(self.label_45)

        self.Setting_Px1_Triangle = QTextEdit(self.widget_39)
        self.Setting_Px1_Triangle.setObjectName(u"Setting_Px1_Triangle")
        self.Setting_Px1_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Px1_Triangle.setFont(font)
        self.Setting_Px1_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_38.addWidget(self.Setting_Px1_Triangle)


        self.verticalLayout_45.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget_19)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.widget_40)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(50, 30))
        self.label_46.setFont(font)

        self.horizontalLayout_39.addWidget(self.label_46)

        self.Setting_Py1_Triangle = QTextEdit(self.widget_40)
        self.Setting_Py1_Triangle.setObjectName(u"Setting_Py1_Triangle")
        self.Setting_Py1_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Py1_Triangle.setFont(font)
        self.Setting_Py1_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_39.addWidget(self.Setting_Py1_Triangle)


        self.verticalLayout_45.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.widget_19)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.widget_41)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(50, 30))
        self.label_47.setFont(font)

        self.horizontalLayout_40.addWidget(self.label_47)

        self.Setting_Pz1_Triangle = QTextEdit(self.widget_41)
        self.Setting_Pz1_Triangle.setObjectName(u"Setting_Pz1_Triangle")
        self.Setting_Pz1_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Pz1_Triangle.setFont(font)
        self.Setting_Pz1_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_40.addWidget(self.Setting_Pz1_Triangle)


        self.verticalLayout_45.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget_19)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.widget_42)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(50, 30))
        self.label_48.setFont(font)

        self.horizontalLayout_41.addWidget(self.label_48)

        self.Setting_Px2_Triangle = QTextEdit(self.widget_42)
        self.Setting_Px2_Triangle.setObjectName(u"Setting_Px2_Triangle")
        self.Setting_Px2_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Px2_Triangle.setFont(font)
        self.Setting_Px2_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_41.addWidget(self.Setting_Px2_Triangle)


        self.verticalLayout_45.addWidget(self.widget_42)

        self.widget_43 = QWidget(self.widget_19)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.widget_43)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(50, 30))
        self.label_49.setFont(font)

        self.horizontalLayout_42.addWidget(self.label_49)

        self.Setting_Py2_Triangle = QTextEdit(self.widget_43)
        self.Setting_Py2_Triangle.setObjectName(u"Setting_Py2_Triangle")
        self.Setting_Py2_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Py2_Triangle.setFont(font)
        self.Setting_Py2_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_42.addWidget(self.Setting_Py2_Triangle)


        self.verticalLayout_45.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.widget_19)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.widget_44)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(50, 30))
        self.label_50.setFont(font)

        self.horizontalLayout_43.addWidget(self.label_50)

        self.Setting_Pz2_Triangle = QTextEdit(self.widget_44)
        self.Setting_Pz2_Triangle.setObjectName(u"Setting_Pz2_Triangle")
        self.Setting_Pz2_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Pz2_Triangle.setFont(font)
        self.Setting_Pz2_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_43.addWidget(self.Setting_Pz2_Triangle)


        self.verticalLayout_45.addWidget(self.widget_44)

        self.widget_46 = QWidget(self.widget_19)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.widget_46)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(50, 30))
        self.label_52.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_52)

        self.Setting_Px3_Triangle = QTextEdit(self.widget_46)
        self.Setting_Px3_Triangle.setObjectName(u"Setting_Px3_Triangle")
        self.Setting_Px3_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Px3_Triangle.setFont(font)
        self.Setting_Px3_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_45.addWidget(self.Setting_Px3_Triangle)


        self.verticalLayout_45.addWidget(self.widget_46)

        self.widget_45 = QWidget(self.widget_19)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.widget_45)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(50, 30))
        self.label_51.setFont(font)

        self.horizontalLayout_44.addWidget(self.label_51)

        self.Setting_Py3_Triangle = QTextEdit(self.widget_45)
        self.Setting_Py3_Triangle.setObjectName(u"Setting_Py3_Triangle")
        self.Setting_Py3_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Py3_Triangle.setFont(font)
        self.Setting_Py3_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_44.addWidget(self.Setting_Py3_Triangle)


        self.verticalLayout_45.addWidget(self.widget_45)

        self.widget_47 = QWidget(self.widget_19)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.widget_47)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(50, 30))
        self.label_53.setFont(font)

        self.horizontalLayout_46.addWidget(self.label_53)

        self.Setting_Pz3_Triangle = QTextEdit(self.widget_47)
        self.Setting_Pz3_Triangle.setObjectName(u"Setting_Pz3_Triangle")
        self.Setting_Pz3_Triangle.setMaximumSize(QSize(70, 30))
        self.Setting_Pz3_Triangle.setFont(font)
        self.Setting_Pz3_Triangle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_46.addWidget(self.Setting_Pz3_Triangle)


        self.verticalLayout_45.addWidget(self.widget_47)


        self.verticalLayout_38.addWidget(self.widget_19)


        self.horizontalLayout_17.addWidget(self.Setting_Triangle)

        self.Setting_Circle = QWidget(self.pageSetting)
        self.Setting_Circle.setObjectName(u"Setting_Circle")
        self.verticalLayout_40 = QVBoxLayout(self.Setting_Circle)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.Setting_Circle)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_41 = QVBoxLayout(self.widget_20)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout_41.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.verticalLayout_40.addWidget(self.widget_20, 0, Qt.AlignTop)

        self.widget_21 = QWidget(self.Setting_Circle)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy2.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy2)
        self.widget_21.setStyleSheet(u"background-color: rgb(109, 109, 109);")
        self.verticalLayout_46 = QVBoxLayout(self.widget_21)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.widget_53 = QWidget(self.widget_21)
        self.widget_53.setObjectName(u"widget_53")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.widget_53)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(50, 30))
        self.label_64.setFont(font)

        self.horizontalLayout_57.addWidget(self.label_64, 0, Qt.AlignHCenter)

        self.Setting_Px_Circle = QTextEdit(self.widget_53)
        self.Setting_Px_Circle.setObjectName(u"Setting_Px_Circle")
        self.Setting_Px_Circle.setMaximumSize(QSize(70, 30))
        self.Setting_Px_Circle.setFont(font)
        self.Setting_Px_Circle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_57.addWidget(self.Setting_Px_Circle)


        self.verticalLayout_46.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.widget_21)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.widget_54)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(50, 30))
        self.label_65.setFont(font)

        self.horizontalLayout_58.addWidget(self.label_65, 0, Qt.AlignHCenter)

        self.Setting_PyCircle = QTextEdit(self.widget_54)
        self.Setting_PyCircle.setObjectName(u"Setting_PyCircle")
        self.Setting_PyCircle.setMaximumSize(QSize(70, 30))
        self.Setting_PyCircle.setFont(font)
        self.Setting_PyCircle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_58.addWidget(self.Setting_PyCircle)


        self.verticalLayout_46.addWidget(self.widget_54)

        self.widget_49 = QWidget(self.widget_21)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.widget_49)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(50, 30))
        self.label_60.setFont(font)

        self.horizontalLayout_53.addWidget(self.label_60, 0, Qt.AlignHCenter)

        self.Setting_Pz_Circle = QTextEdit(self.widget_49)
        self.Setting_Pz_Circle.setObjectName(u"Setting_Pz_Circle")
        self.Setting_Pz_Circle.setMaximumSize(QSize(70, 30))
        self.Setting_Pz_Circle.setFont(font)
        self.Setting_Pz_Circle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_53.addWidget(self.Setting_Pz_Circle)


        self.verticalLayout_46.addWidget(self.widget_49)

        self.widget_55 = QWidget(self.widget_21)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.widget_55)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(50, 30))
        self.label_66.setFont(font)

        self.horizontalLayout_59.addWidget(self.label_66, 0, Qt.AlignHCenter)

        self.Setting_Radius_Circle = QTextEdit(self.widget_55)
        self.Setting_Radius_Circle.setObjectName(u"Setting_Radius_Circle")
        self.Setting_Radius_Circle.setMaximumSize(QSize(70, 30))
        self.Setting_Radius_Circle.setFont(font)
        self.Setting_Radius_Circle.setStyleSheet(u"border-color: rgb(0, 255, 0);")

        self.horizontalLayout_59.addWidget(self.Setting_Radius_Circle)


        self.verticalLayout_46.addWidget(self.widget_55)


        self.verticalLayout_40.addWidget(self.widget_21)


        self.horizontalLayout_17.addWidget(self.Setting_Circle)

        self.stackedWidget_2.addWidget(self.pageSetting)
        self.pageInfo = QWidget()
        self.pageInfo.setObjectName(u"pageInfo")
        self.verticalLayout_85 = QVBoxLayout(self.pageInfo)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.label_3 = QLabel(self.pageInfo)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)

        self.verticalLayout_85.addWidget(self.label_3)

        self.label_38 = QLabel(self.pageInfo)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.verticalLayout_85.addWidget(self.label_38)

        self.label_122 = QLabel(self.pageInfo)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font3)

        self.verticalLayout_85.addWidget(self.label_122)

        self.label_124 = QLabel(self.pageInfo)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font3)

        self.verticalLayout_85.addWidget(self.label_124)

        self.label_125 = QLabel(self.pageInfo)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font3)

        self.verticalLayout_85.addWidget(self.label_125)

        self.label_126 = QLabel(self.pageInfo)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font3)

        self.verticalLayout_85.addWidget(self.label_126)

        self.label_127 = QLabel(self.pageInfo)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font3)

        self.verticalLayout_85.addWidget(self.label_127)

        self.stackedWidget_2.addWidget(self.pageInfo)

        self.verticalLayout_10.addWidget(self.stackedWidget_2, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.Body)

        self.popupNotification = QCustomSlideMenu(self.mainBody)
        self.popupNotification.setObjectName(u"popupNotification")
        self.verticalLayout_16 = QVBoxLayout(self.popupNotification)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.popupNotificationSub = QWidget(self.popupNotification)
        self.popupNotificationSub.setObjectName(u"popupNotificationSub")
        self.verticalLayout_17 = QVBoxLayout(self.popupNotificationSub)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.popupNotificationSub)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_17.addWidget(self.label_10)

        self.frame_8 = QFrame(self.popupNotificationSub)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_content_Notification = QLabel(self.frame_8)
        self.lbl_content_Notification.setObjectName(u"lbl_content_Notification")
        sizePolicy1.setHeightForWidth(self.lbl_content_Notification.sizePolicy().hasHeightForWidth())
        self.lbl_content_Notification.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.lbl_content_Notification.setFont(font4)

        self.horizontalLayout_8.addWidget(self.lbl_content_Notification)

        self.CloseNotificationBtn = QPushButton(self.frame_8)
        self.CloseNotificationBtn.setObjectName(u"CloseNotificationBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseNotificationBtn.setIcon(icon12)
        self.CloseNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.CloseNotificationBtn)


        self.verticalLayout_17.addWidget(self.frame_8)


        self.verticalLayout_16.addWidget(self.popupNotificationSub)


        self.verticalLayout_9.addWidget(self.popupNotification)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_9 = QHBoxLayout(self.footer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.footer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_11.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.sizeGrip)


        self.verticalLayout_9.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.connectBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Conncect", None))
#endif // QT_CONFIG(tooltip)
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
#if QT_CONFIG(tooltip)
        self.kinematicBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Kinematic", None))
#endif // QT_CONFIG(tooltip)
        self.kinematicBtn.setText(QCoreApplication.translate("MainWindow", u"Kinematic", None))
#if QT_CONFIG(tooltip)
        self.trajectoryBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Trajectory", None))
#endif // QT_CONFIG(tooltip)
        self.trajectoryBtn.setText(QCoreApplication.translate("MainWindow", u"Trajectory", None))
#if QT_CONFIG(tooltip)
        self.signalBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Signal", None))
#endif // QT_CONFIG(tooltip)
        self.signalBtn.setText(QCoreApplication.translate("MainWindow", u"Signal Output", None))
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.aboutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(tooltip)
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DATA TRANSFER MODE:", None))
        self.lbl_DataStatus.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
#if QT_CONFIG(tooltip)
        self.notificatioBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notification", None))
#endif // QT_CONFIG(tooltip)
        self.notificatioBtn.setText("")
#if QT_CONFIG(tooltip)
        self.MinimizeWinBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.MinimizeWinBtn.setText("")
#if QT_CONFIG(tooltip)
        self.RestoreWinBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.RestoreWinBtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseWinBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.CloseWinBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HO CHI MINH CITY UNIVERSITY OF TECHNOLOGY AND EDUCATION", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"PROJECT : DESIGN AND CONTROL 6-DOF CABLE MANIPULATOR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"COM:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"BAUDRATE:", None))
        self.cbbBaudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.cbbBaudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"115200", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"DATA MODE:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"ON/OFF", None))
        self.UpdatePortBtn.setText(QCoreApplication.translate("MainWindow", u"Update Port", None))
        self.ConnectedBtn.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"KINEMATIC", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Theta1:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Theta2:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Theta3:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Theta4:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Theta5:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Theta6:", None))
        self.textEdit_FK_t1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0.00</span></p></body></html>", None))
        self.textEdit_FK_t2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0.00</span></p></body></html>", None))
        self.textEdit_FK_t3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0.00</span></p></body></html>", None))
        self.textEdit_FK_t4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0.00</span></p></body></html>", None))
        self.textEdit_FK_t5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0.00</span></p></body></html>", None))
        self.textEdit_FK_t6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0.00</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Px:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Py:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Pz:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Alpha:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Beta", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Gama", None))
        self.FK_Px.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.FK_Py.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.FK_Pz.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.alpha.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.beta.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.gama.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.Solve_FK.setText(QCoreApplication.translate("MainWindow", u"SOLVE FORWARD", None))
        self.Solve_IK.setText(QCoreApplication.translate("MainWindow", u"SOLVE INVERSE ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Trajectory Status:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.Stop_draw.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Lines.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.Triangles.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.Circles.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.SignalOutputBtn.setText(QCoreApplication.translate("MainWindow", u"Signal Output", None))
        self.SignalErrorBtn.setText(QCoreApplication.translate("MainWindow", u"Signal Error", None))
        self.PositionOutputBtn.setText(QCoreApplication.translate("MainWindow", u"Position Output", None))
        self.PositionErrorBtn.setText(QCoreApplication.translate("MainWindow", u"Position Error", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Theta Inital", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Theta1:", None))
        self.Setting_Theta1_init.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">45</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Theta2:", None))
        self.Setting_Theta2_init.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">-30</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Theta3:", None))
        self.Setting_Theta3_init.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Theta4:", None))
        self.Setting_Theta4_init.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Theta5:", None))
        self.Setting_Theta5_init.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Theta6:", None))
        self.Setting_Theta6_init.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home Point Setting", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Px:", None))
        self.Setting_Px_Home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">835</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Py:", None))
        self.Setting_Py_Home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Pz:", None))
        self.Setting_Pz_Home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"L1:", None))
        self.Setting_L1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">170</span></p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"L2:", None))
        self.Setting_L2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">225</span></p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"L3:", None))
        self.Setting_L3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">225</span></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"L4:", None))
        self.Setting_L4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">215</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Line Setting", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Px1:", None))
        self.Setting_Px1_Line.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">780</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Py1:", None))
        self.Setting_Py1_Line.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">100</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Pz1:", None))
        self.Setting_Pz1_Line.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">50</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Px2:", None))
        self.Setting_Px2_Line.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">780</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Py2:", None))
        self.Setting_Py2_Line.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">-100</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Pz2:", None))
        self.Setting_Pz2_Line.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">50</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Triangle Setting", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Px1:", None))
        self.Setting_Px1_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">780</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Py1:", None))
        self.Setting_Py1_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Pz1:", None))
        self.Setting_Pz1_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">50</span></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Px2:", None))
        self.Setting_Px2_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">780</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Py2:", None))
        self.Setting_Py2_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">50</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Pz2:", None))
        self.Setting_Pz2_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Px3:", None))
        self.Setting_Px3_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">780</span></p></body></html>", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Py3:", None))
        self.Setting_Py3_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">-50</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Pz3:", None))
        self.Setting_Pz3_Triangle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Circle Setting", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Px:", None))
        self.Setting_Px_Circle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">780</span></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Py:", None))
        self.Setting_PyCircle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Pz:", None))
        self.Setting_Pz_Circle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.Setting_Radius_Circle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">50</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GVHD: Tr\u1ea7n \u0110\u1ee9c Thi\u1ec7n - 0988862588 - thientd@hcmute.edu.vn", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Th\u00e0nh vi\u00ean 1: Tr\u1ea7n Tr\u1ecdng L\u01b0\u1ee3ng - 0702825501  - luongtt.works@gmail.com", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Th\u00e0nh vi\u00ean 2: D\u01b0\u01a1ng Minh Tr\u00ed - 0934320877 - tri.dm2000@gmail.com", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Fanpage: https://www.facebook.com/RICLab.hcmute.vn", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Website: https://www.riclab-ute.com/", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9: Ph\u00f2ng C205, Tr\u01b0\u1eddng \u0111\u1ea1i h\u1ecdc S\u01b0 Ph\u1ea1m K\u1ef9 Thu\u1eadt th\u00e0nh ph\u1ed1 H\u1ed3 Ch\u00ed Minh", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Chi ti\u1ebft thu\u1eadt to\u00e1n : https://ieeexplore.ieee.org/abstract/document/9997795/", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.lbl_content_Notification.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.CloseNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification Message", None))
#endif // QT_CONFIG(tooltip)
        self.CloseNotificationBtn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ROBOTIC AND INTELLIGENT CONTROL ( RICLAB) - 6-DOF CABLE MANIPULATOR", None))
    # retranslateUi

