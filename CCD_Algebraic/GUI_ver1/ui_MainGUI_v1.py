# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainGUI_v1NRtfLG.ui'
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
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.connectBtn = QPushButton(self.frame_2)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.connectBtn.setIcon(icon2)
        self.connectBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.connectBtn)

        self.kinematicBtn = QPushButton(self.frame_2)
        self.kinematicBtn.setObjectName(u"kinematicBtn")
        self.kinematicBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.kinematicBtn.setIcon(icon3)
        self.kinematicBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.kinematicBtn)

        self.trajectoryBtn = QPushButton(self.frame_2)
        self.trajectoryBtn.setObjectName(u"trajectoryBtn")
        self.trajectoryBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/bookmark.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.trajectoryBtn.setIcon(icon4)
        self.trajectoryBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.trajectoryBtn)

        self.signalBtn = QPushButton(self.frame_2)
        self.signalBtn.setObjectName(u"signalBtn")
        self.signalBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/trello.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon6.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon6)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingBtn)

        self.aboutBtn = QPushButton(self.frame_3)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon7)
        self.aboutBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.aboutBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSub)


        self.horizontalLayout.addWidget(self.leftMenu, 0, Qt.AlignLeft)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSub = QWidget(self.centerMenu)
        self.centerMenuSub.setObjectName(u"centerMenuSub")
        self.centerMenuSub.setMinimumSize(QSize(250, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSub)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centerMenuSub)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.CloseMoreMenuBtn = QPushButton(self.frame_4)
        self.CloseMoreMenuBtn.setObjectName(u"CloseMoreMenuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseMoreMenuBtn.setIcon(icon8)
        self.CloseMoreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.CloseMoreMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QCustomStackedWidget(self.centerMenuSub)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_7 = QVBoxLayout(self.page_settings)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_settings)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.top = QWidget(self.frame_10)
        self.top.setObjectName(u"top")
        self.verticalLayout_19 = QVBoxLayout(self.top)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.top)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_12.setFont(font1)

        self.verticalLayout_19.addWidget(self.label_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.top, 0, Qt.AlignTop)

        self.body = QWidget(self.frame_10)
        self.body.setObjectName(u"body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setMaximumSize(QSize(16777215, 400))
        self.body.setFont(font)
        self.verticalLayout_20 = QVBoxLayout(self.body)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.theta1 = QFrame(self.body)
        self.theta1.setObjectName(u"theta1")
        self.theta1.setFrameShape(QFrame.StyledPanel)
        self.theta1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.theta1)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.theta1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(60, 30))
        self.label_13.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.textEdit_init_t1 = QTextEdit(self.theta1)
        self.textEdit_init_t1.setObjectName(u"textEdit_init_t1")
        self.textEdit_init_t1.setMinimumSize(QSize(0, 0))
        self.textEdit_init_t1.setMaximumSize(QSize(60, 30))
        self.textEdit_init_t1.setFont(font)
        self.textEdit_init_t1.setTabStopWidth(80)

        self.horizontalLayout_11.addWidget(self.textEdit_init_t1)


        self.verticalLayout_20.addWidget(self.theta1)

        self.theta2 = QFrame(self.body)
        self.theta2.setObjectName(u"theta2")
        self.theta2.setFrameShape(QFrame.StyledPanel)
        self.theta2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.theta2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.theta2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(60, 30))
        self.label_14.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.textEdit_init_t2 = QTextEdit(self.theta2)
        self.textEdit_init_t2.setObjectName(u"textEdit_init_t2")
        self.textEdit_init_t2.setMaximumSize(QSize(60, 30))
        self.textEdit_init_t2.setFont(font)

        self.horizontalLayout_12.addWidget(self.textEdit_init_t2)


        self.verticalLayout_20.addWidget(self.theta2)

        self.theta3 = QFrame(self.body)
        self.theta3.setObjectName(u"theta3")
        self.theta3.setFrameShape(QFrame.StyledPanel)
        self.theta3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.theta3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.theta3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(60, 30))
        self.label_15.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.textEdit_init_t3 = QTextEdit(self.theta3)
        self.textEdit_init_t3.setObjectName(u"textEdit_init_t3")
        self.textEdit_init_t3.setMaximumSize(QSize(60, 30))
        self.textEdit_init_t3.setFont(font)

        self.horizontalLayout_13.addWidget(self.textEdit_init_t3)


        self.verticalLayout_20.addWidget(self.theta3)

        self.theta4 = QFrame(self.body)
        self.theta4.setObjectName(u"theta4")
        self.theta4.setFrameShape(QFrame.StyledPanel)
        self.theta4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.theta4)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.theta4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(60, 30))
        self.label_16.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_16)

        self.textEdit_init_t4 = QTextEdit(self.theta4)
        self.textEdit_init_t4.setObjectName(u"textEdit_init_t4")
        self.textEdit_init_t4.setMaximumSize(QSize(60, 30))
        self.textEdit_init_t4.setFont(font)

        self.horizontalLayout_14.addWidget(self.textEdit_init_t4)


        self.verticalLayout_20.addWidget(self.theta4)

        self.theta5 = QFrame(self.body)
        self.theta5.setObjectName(u"theta5")
        self.theta5.setFrameShape(QFrame.StyledPanel)
        self.theta5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.theta5)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.theta5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(60, 30))
        self.label_17.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_17)

        self.textEdit_init_t5 = QTextEdit(self.theta5)
        self.textEdit_init_t5.setObjectName(u"textEdit_init_t5")
        self.textEdit_init_t5.setMaximumSize(QSize(60, 30))
        self.textEdit_init_t5.setFont(font)

        self.horizontalLayout_15.addWidget(self.textEdit_init_t5)


        self.verticalLayout_20.addWidget(self.theta5)

        self.theta6 = QFrame(self.body)
        self.theta6.setObjectName(u"theta6")
        self.theta6.setFrameShape(QFrame.StyledPanel)
        self.theta6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.theta6)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.theta6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(60, 30))
        self.label_18.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_18)

        self.textEdit_init_t6 = QTextEdit(self.theta6)
        self.textEdit_init_t6.setObjectName(u"textEdit_init_t6")
        self.textEdit_init_t6.setMaximumSize(QSize(60, 30))
        self.textEdit_init_t6.setFont(font)

        self.horizontalLayout_16.addWidget(self.textEdit_init_t6)


        self.verticalLayout_20.addWidget(self.theta6)

        self.L1 = QFrame(self.body)
        self.L1.setObjectName(u"L1")
        self.L1.setFrameShape(QFrame.StyledPanel)
        self.L1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.L1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.L1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(60, 30))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_19.setFont(font2)

        self.horizontalLayout_17.addWidget(self.label_19)

        self.textEdit_L1 = QTextEdit(self.L1)
        self.textEdit_L1.setObjectName(u"textEdit_L1")
        self.textEdit_L1.setMaximumSize(QSize(60, 30))
        self.textEdit_L1.setFont(font)

        self.horizontalLayout_17.addWidget(self.textEdit_L1)


        self.verticalLayout_20.addWidget(self.L1)

        self.L2 = QFrame(self.body)
        self.L2.setObjectName(u"L2")
        self.L2.setFrameShape(QFrame.StyledPanel)
        self.L2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.L2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.L2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(60, 30))
        self.label_20.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_20)

        self.textEdit_L2 = QTextEdit(self.L2)
        self.textEdit_L2.setObjectName(u"textEdit_L2")
        self.textEdit_L2.setMaximumSize(QSize(60, 30))
        self.textEdit_L2.setFont(font)

        self.horizontalLayout_18.addWidget(self.textEdit_L2)


        self.verticalLayout_20.addWidget(self.L2)

        self.L3 = QFrame(self.body)
        self.L3.setObjectName(u"L3")
        self.L3.setFrameShape(QFrame.StyledPanel)
        self.L3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.L3)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.L3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(60, 30))
        self.label_21.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_21)

        self.textEdit_L3 = QTextEdit(self.L3)
        self.textEdit_L3.setObjectName(u"textEdit_L3")
        self.textEdit_L3.setMaximumSize(QSize(60, 30))
        self.textEdit_L3.setFont(font)

        self.horizontalLayout_19.addWidget(self.textEdit_L3)


        self.verticalLayout_20.addWidget(self.L3)

        self.L4 = QFrame(self.body)
        self.L4.setObjectName(u"L4")
        self.L4.setFrameShape(QFrame.StyledPanel)
        self.L4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.L4)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.L4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(60, 30))
        self.label_22.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_22)

        self.textEdit_L4 = QTextEdit(self.L4)
        self.textEdit_L4.setObjectName(u"textEdit_L4")
        self.textEdit_L4.setMaximumSize(QSize(60, 30))
        self.textEdit_L4.setFont(font)

        self.horizontalLayout_20.addWidget(self.textEdit_L4)


        self.verticalLayout_20.addWidget(self.L4)


        self.verticalLayout_18.addWidget(self.body)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)

        self.Bottom = QFrame(self.frame_10)
        self.Bottom.setObjectName(u"Bottom")
        self.Bottom.setMaximumSize(QSize(16777215, 40))
        self.Bottom.setFrameShape(QFrame.StyledPanel)
        self.Bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.Bottom)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.Bottom)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_21.addWidget(self.pushButton)


        self.verticalLayout_18.addWidget(self.Bottom)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayout_8 = QVBoxLayout(self.page_info)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_info)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.centerMenuSub, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy3)
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificatioBtn.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeWinBtn.setIcon(icon10)
        self.MinimizeWinBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.MinimizeWinBtn)

        self.RestoreWinBtn = QPushButton(self.frame_7)
        self.RestoreWinBtn.setObjectName(u"RestoreWinBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RestoreWinBtn.setIcon(icon11)
        self.RestoreWinBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.RestoreWinBtn)

        self.CloseWinBtn = QPushButton(self.frame_7)
        self.CloseWinBtn.setObjectName(u"CloseWinBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseWinBtn.setIcon(icon12)
        self.CloseWinBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.CloseWinBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.Header, 0, Qt.AlignTop)

        self.Body = QWidget(self.mainBody)
        self.Body.setObjectName(u"Body")
        sizePolicy1.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.Body)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.stackedWidget_2 = QCustomStackedWidget(self.Body)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_11 = QVBoxLayout(self.pageHome)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.pageHome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_11.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.pageHome)
        self.pageConnected = QWidget()
        self.pageConnected.setObjectName(u"pageConnected")
        self.verticalLayout_12 = QVBoxLayout(self.pageConnected)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pageConnect_Top = QFrame(self.pageConnected)
        self.pageConnect_Top.setObjectName(u"pageConnect_Top")
        self.pageConnect_Top.setFrameShape(QFrame.StyledPanel)
        self.pageConnect_Top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.pageConnect_Top)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_11 = QFrame(self.pageConnect_Top)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 30))
        self.label_5.setFont(font)

        self.verticalLayout_22.addWidget(self.label_5)

        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(110, 30))
        self.label_23.setFont(font)

        self.verticalLayout_22.addWidget(self.label_23)


        self.horizontalLayout_22.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.pageConnect_Top)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.comboBox = QComboBox(self.frame_12)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(150, 30))
        self.comboBox.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.verticalLayout_23.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.frame_12)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(150, 30))
        self.comboBox_2.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.verticalLayout_23.addWidget(self.comboBox_2)


        self.horizontalLayout_22.addWidget(self.frame_12)


        self.verticalLayout_12.addWidget(self.pageConnect_Top)

        self.pageConnect_Bottom = QFrame(self.pageConnected)
        self.pageConnect_Bottom.setObjectName(u"pageConnect_Bottom")
        sizePolicy.setHeightForWidth(self.pageConnect_Bottom.sizePolicy().hasHeightForWidth())
        self.pageConnect_Bottom.setSizePolicy(sizePolicy)
        self.pageConnect_Bottom.setFrameShape(QFrame.StyledPanel)
        self.pageConnect_Bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.pageConnect_Bottom)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Connected = QPushButton(self.pageConnect_Bottom)
        self.Connected.setObjectName(u"Connected")
        sizePolicy.setHeightForWidth(self.Connected.sizePolicy().hasHeightForWidth())
        self.Connected.setSizePolicy(sizePolicy)
        self.Connected.setMaximumSize(QSize(200, 60))
        self.Connected.setFont(font)
        self.Connected.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout_23.addWidget(self.Connected)

        self.Disconected = QPushButton(self.pageConnect_Bottom)
        self.Disconected.setObjectName(u"Disconected")
        self.Disconected.setMaximumSize(QSize(200, 60))
        self.Disconected.setFont(font)
        self.Disconected.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout_23.addWidget(self.Disconected)


        self.verticalLayout_12.addWidget(self.pageConnect_Bottom)

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
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
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
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_20)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.slider_t1 = QSlider(self.frame_20)
        self.slider_t1.setObjectName(u"slider_t1")
        self.slider_t1.setMaximumSize(QSize(200, 30))
        self.slider_t1.setMinimum(-45)
        self.slider_t1.setMaximum(45)
        self.slider_t1.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t1)

        self.slider_t2 = QSlider(self.frame_20)
        self.slider_t2.setObjectName(u"slider_t2")
        self.slider_t2.setMaximumSize(QSize(200, 30))
        self.slider_t2.setMinimum(-30)
        self.slider_t2.setMaximum(45)
        self.slider_t2.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t2)

        self.slider_t3 = QSlider(self.frame_20)
        self.slider_t3.setObjectName(u"slider_t3")
        self.slider_t3.setMaximumSize(QSize(200, 30))
        self.slider_t3.setMinimum(-45)
        self.slider_t3.setMaximum(45)
        self.slider_t3.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t3)

        self.slider_t4 = QSlider(self.frame_20)
        self.slider_t4.setObjectName(u"slider_t4")
        self.slider_t4.setMaximumSize(QSize(200, 30))
        self.slider_t4.setMinimum(-30)
        self.slider_t4.setMaximum(45)
        self.slider_t4.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t4)

        self.slider_t5 = QSlider(self.frame_20)
        self.slider_t5.setObjectName(u"slider_t5")
        self.slider_t5.setMaximumSize(QSize(200, 30))
        self.slider_t5.setMinimum(-45)
        self.slider_t5.setMaximum(45)
        self.slider_t5.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.slider_t5)

        self.slider_t6 = QSlider(self.frame_20)
        self.slider_t6.setObjectName(u"slider_t6")
        self.slider_t6.setMaximumSize(QSize(200, 30))
        self.slider_t6.setMinimum(-45)
        self.slider_t6.setMaximum(45)
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
        self.textEdit_FK_t1.setMaximumSize(QSize(60, 30))
        self.textEdit_FK_t1.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t1)

        self.textEdit_FK_t2 = QTextEdit(self.frame_17)
        self.textEdit_FK_t2.setObjectName(u"textEdit_FK_t2")
        self.textEdit_FK_t2.setMaximumSize(QSize(60, 30))
        self.textEdit_FK_t2.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t2)

        self.textEdit_FK_t3 = QTextEdit(self.frame_17)
        self.textEdit_FK_t3.setObjectName(u"textEdit_FK_t3")
        self.textEdit_FK_t3.setMaximumSize(QSize(60, 30))
        self.textEdit_FK_t3.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t3)

        self.textEdit_FK_t4 = QTextEdit(self.frame_17)
        self.textEdit_FK_t4.setObjectName(u"textEdit_FK_t4")
        self.textEdit_FK_t4.setMaximumSize(QSize(60, 30))
        self.textEdit_FK_t4.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t4)

        self.textEdit_FK_t5 = QTextEdit(self.frame_17)
        self.textEdit_FK_t5.setObjectName(u"textEdit_FK_t5")
        self.textEdit_FK_t5.setMaximumSize(QSize(60, 30))
        self.textEdit_FK_t5.setFont(font)

        self.verticalLayout_27.addWidget(self.textEdit_FK_t5)

        self.textEdit_FK_t6 = QTextEdit(self.frame_17)
        self.textEdit_FK_t6.setObjectName(u"textEdit_FK_t6")
        self.textEdit_FK_t6.setMaximumSize(QSize(60, 30))
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


        self.verticalLayout_21.addWidget(self.pageKinematic_body, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.pageKinematic)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
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

        self.Solve_FK_2 = QPushButton(self.frame_14)
        self.Solve_FK_2.setObjectName(u"Solve_FK_2")
        self.Solve_FK_2.setMaximumSize(QSize(200, 40))
        self.Solve_FK_2.setFont(font)
        self.Solve_FK_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_27.addWidget(self.Solve_FK_2)


        self.verticalLayout_13.addWidget(self.frame_14)

        self.stackedWidget_2.addWidget(self.pageKinematic)
        self.pageTrajectory = QWidget()
        self.pageTrajectory.setObjectName(u"pageTrajectory")
        self.verticalLayout_14 = QVBoxLayout(self.pageTrajectory)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.pageTrajectory)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_14.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.stackedWidget_2.addWidget(self.pageTrajectory)
        self.pageSignal = QWidget()
        self.pageSignal.setObjectName(u"pageSignal")
        self.verticalLayout_15 = QVBoxLayout(self.pageSignal)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.pageSignal)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_15.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.stackedWidget_2.addWidget(self.pageSignal)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)


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
        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_9.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.CloseNotificationBtn = QPushButton(self.frame_8)
        self.CloseNotificationBtn.setObjectName(u"CloseNotificationBtn")
        self.CloseNotificationBtn.setIcon(icon8)
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
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_11.setFont(font4)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.CloseMoreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close More Menu", None))
#endif // QT_CONFIG(tooltip)
        self.CloseMoreMenuBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Initial", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Theta1:", None))
        self.textEdit_init_t1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">-30</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Theta2:", None))
        self.textEdit_init_t2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">40</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Theta3:", None))
        self.textEdit_init_t3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Theta4:", None))
        self.textEdit_init_t4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Theta5:", None))
        self.textEdit_init_t5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Theta6:", None))
        self.textEdit_init_t6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"L1", None))
        self.textEdit_L1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">120</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"L2:", None))
        self.textEdit_L2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">225</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"L3:", None))
        self.textEdit_L3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">225</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"L4:", None))
        self.textEdit_L4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">215</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"6-DOF CABLE MANIPULATOR", None))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"COM:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"BAUDRATE:", None))
        self.Connected.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.Disconected.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.textEdit_FK_t2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.textEdit_FK_t3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.textEdit_FK_t4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.textEdit_FK_t5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
        self.textEdit_FK_t6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">0</span></p></body></html>", None))
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
        self.Solve_FK_2.setText(QCoreApplication.translate("MainWindow", u"SOLVE INVERSE ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Trajectory", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Signal Output", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.CloseNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification Message", None))
#endif // QT_CONFIG(tooltip)
        self.CloseNotificationBtn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ROBOTIC AND INTELLIGENT CONTROL - RICLAB", None))
    # retranslateUi

