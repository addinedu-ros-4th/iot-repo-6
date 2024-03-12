# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingcvFOx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 900)
        MainWindow.setMinimumSize(QSize(1332, 900))
        MainWindow.setMaximumSize(QSize(1332, 900))
        MainWindow.setStyleSheet(u"background-color: rgb(77, 77, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarTEMP = QFrame(self.centralwidget)
        self.circularProgressBarTEMP.setObjectName(u"circularProgressBarTEMP")
        self.circularProgressBarTEMP.setGeometry(QRect(260, 80, 240, 240))
        self.circularProgressBarTEMP.setStyleSheet(u"background-color: none;")
        self.circularProgressBarTEMP.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarTEMP.setFrameShadow(QFrame.Raised)
        self.circularProgressTEMP = QFrame(self.circularProgressBarTEMP)
        self.circularProgressTEMP.setObjectName(u"circularProgressTEMP")
        self.circularProgressTEMP.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressTEMP.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(255, 0, 127, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressTEMP.setFrameShape(QFrame.StyledPanel)
        self.circularProgressTEMP.setFrameShadow(QFrame.Raised)
        self.circularBgTEMP = QFrame(self.circularProgressBarTEMP)
        self.circularBgTEMP.setObjectName(u"circularBgTEMP")
        self.circularBgTEMP.setGeometry(QRect(10, 10, 220, 220))
        self.circularBgTEMP.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBgTEMP.setFrameShape(QFrame.StyledPanel)
        self.circularBgTEMP.setFrameShadow(QFrame.Raised)
        self.circularContainerTEMP = QFrame(self.circularProgressBarTEMP)
        self.circularContainerTEMP.setObjectName(u"circularContainerTEMP")
        self.circularContainerTEMP.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainerTEMP.setBaseSize(QSize(0, 0))
        self.circularContainerTEMP.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainerTEMP.setFrameShape(QFrame.StyledPanel)
        self.circularContainerTEMP.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.circularContainerTEMP)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 171, 137))
        self.infoLayout = QGridLayout(self.layoutWidget)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTEMP = QLabel(self.layoutWidget)
        self.labelTEMP.setObjectName(u"labelTEMP")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.labelTEMP.setFont(font)
        self.labelTEMP.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelTEMP.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelTEMP, 0, 0, 1, 1)

        self.labelDegreeTEMP = QLabel(self.layoutWidget)
        self.labelDegreeTEMP.setObjectName(u"labelDegreeTEMP")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(30)
        self.labelDegreeTEMP.setFont(font1)
        self.labelDegreeTEMP.setStyleSheet(u"color: rgb(255, 44, 174); padding: 0px; background-color: none;")
        self.labelDegreeTEMP.setAlignment(Qt.AlignCenter)
        self.labelDegreeTEMP.setIndent(-1)

        self.infoLayout.addWidget(self.labelDegreeTEMP, 1, 0, 1, 1)

        self.labelCredits = QLabel(self.layoutWidget)
        self.labelCredits.setObjectName(u"labelCredits")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        self.labelCredits.setFont(font2)
        self.labelCredits.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelCredits, 2, 0, 1, 1)

        self.circularBgTEMP.raise_()
        self.circularProgressTEMP.raise_()
        self.circularContainerTEMP.raise_()
        self.circularProgressBarHUM = QFrame(self.centralwidget)
        self.circularProgressBarHUM.setObjectName(u"circularProgressBarHUM")
        self.circularProgressBarHUM.setGeometry(QRect(510, 80, 240, 240))
        self.circularProgressBarHUM.setStyleSheet(u"background-color: none;")
        self.circularProgressBarHUM.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarHUM.setFrameShadow(QFrame.Raised)
        self.circularProgressHUM = QFrame(self.circularProgressBarHUM)
        self.circularProgressHUM.setObjectName(u"circularProgressHUM")
        self.circularProgressHUM.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressHUM.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"       background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.600 rgba(85, 170, 255, 255), stop:0.595 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressHUM.setFrameShape(QFrame.StyledPanel)
        self.circularProgressHUM.setFrameShadow(QFrame.Raised)
        self.circularBgHUM = QFrame(self.circularProgressBarHUM)
        self.circularBgHUM.setObjectName(u"circularBgHUM")
        self.circularBgHUM.setGeometry(QRect(10, 10, 220, 220))
        self.circularBgHUM.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBgHUM.setFrameShape(QFrame.StyledPanel)
        self.circularBgHUM.setFrameShadow(QFrame.Raised)
        self.circularContainerHUM = QFrame(self.circularProgressBarHUM)
        self.circularContainerHUM.setObjectName(u"circularContainerHUM")
        self.circularContainerHUM.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainerHUM.setBaseSize(QSize(0, 0))
        self.circularContainerHUM.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainerHUM.setFrameShape(QFrame.StyledPanel)
        self.circularContainerHUM.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.circularContainerHUM)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 171, 127))
        self.infoLayout_2 = QGridLayout(self.layoutWidget_2)
        self.infoLayout_2.setObjectName(u"infoLayout_2")
        self.infoLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelHUM = QLabel(self.layoutWidget_2)
        self.labelHUM.setObjectName(u"labelHUM")
        self.labelHUM.setFont(font)
        self.labelHUM.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelHUM.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelHUM, 0, 0, 1, 1)

        self.labelPercentageHUM = QLabel(self.layoutWidget_2)
        self.labelPercentageHUM.setObjectName(u"labelPercentageHUM")
        self.labelPercentageHUM.setFont(font1)
        self.labelPercentageHUM.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageHUM.setAlignment(Qt.AlignCenter)
        self.labelPercentageHUM.setIndent(-1)

        self.infoLayout_2.addWidget(self.labelPercentageHUM, 1, 0, 1, 1)

        self.labelCredits_2 = QLabel(self.layoutWidget_2)
        self.labelCredits_2.setObjectName(u"labelCredits_2")
        self.labelCredits_2.setFont(font2)
        self.labelCredits_2.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelCredits_2, 2, 0, 1, 1)

        self.circularBgHUM.raise_()
        self.circularProgressHUM.raise_()
        self.circularContainerHUM.raise_()
        self.circularProgressBarAIR = QFrame(self.centralwidget)
        self.circularProgressBarAIR.setObjectName(u"circularProgressBarAIR")
        self.circularProgressBarAIR.setGeometry(QRect(10, 80, 240, 240))
        self.circularProgressBarAIR.setStyleSheet(u"background-color: none;")
        self.circularProgressBarAIR.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarAIR.setFrameShadow(QFrame.Raised)
        self.circularProgresAIR = QFrame(self.circularProgressBarAIR)
        self.circularProgresAIR.setObjectName(u"circularProgressAIR")
        self.circularProgresAIR.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgresAIR.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(85, 255, 127, 255), stop:0.745 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgresAIR.setFrameShape(QFrame.StyledPanel)
        self.circularProgresAIR.setFrameShadow(QFrame.Raised)
        self.circularBgAIR = QFrame(self.circularProgressBarAIR)
        self.circularBgAIR.setObjectName(u"circularBgAIR")
        self.circularBgAIR.setGeometry(QRect(10, 10, 220, 220))
        self.circularBgAIR.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBgAIR.setFrameShape(QFrame.StyledPanel)
        self.circularBgAIR.setFrameShadow(QFrame.Raised)
        self.circularContainerAIR = QFrame(self.circularProgressBarAIR)
        self.circularContainerAIR.setObjectName(u"circularContainerAIR")
        self.circularContainerAIR.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainerAIR.setBaseSize(QSize(0, 0))
        self.circularContainerAIR.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainerAIR.setFrameShape(QFrame.StyledPanel)
        self.circularContainerAIR.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.circularContainerAIR)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 40, 171, 125))
        self.infoLayout_3 = QGridLayout(self.layoutWidget_3)
        self.infoLayout_3.setObjectName(u"infoLayout_3")
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelAIR = QLabel(self.layoutWidget_3)
        self.labelAIR.setObjectName(u"labelAIR")
        self.labelAIR.setFont(font)
        self.labelAIR.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAIR.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelAIR, 0, 0, 1, 1)

        self.labelCredits_3 = QLabel(self.layoutWidget_3)
        self.labelCredits_3.setObjectName(u"labelCredits_3")
        self.labelCredits_3.setFont(font2)
        self.labelCredits_3.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelCredits_3, 3, 0, 1, 1)

        self.labelPercentageAIR = QLabel(self.layoutWidget_3)
        self.labelPercentageAIR.setObjectName(u"labelPercentageAIR")
        self.labelPercentageAIR.setFont(font1)
        self.labelPercentageAIR.setStyleSheet(u"color: rgb(115, 255, 171); padding: 0px; background-color: none;")
        self.labelPercentageAIR.setAlignment(Qt.AlignCenter)
        self.labelPercentageAIR.setIndent(-1)

        self.infoLayout_3.addWidget(self.labelPercentageAIR, 1, 0, 1, 1)

        self.circularBgAIR.raise_()
        self.circularProgresAIR.raise_()
        self.circularContainerAIR.raise_()
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 10, 641, 50))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(14)
        self.label_title.setFont(font3)
        self.label_title.setStyleSheet(u"color: rgb(115, 185, 255); background-color: none;")
        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(1277, 20, 17, 17))
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        
        self.camera = QLabel(self.centralwidget)
        self.camera.setObjectName(u"camera")
        self.camera.setGeometry(QRect(346, 440, 341, 301))
        # self.camera.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.camera.setFont(font4)
        self.camera.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        
        self.rfid = QLabel(self.centralwidget)
        self.rfid.setObjectName(u"rfid")
        self.rfid.setGeometry(QRect(90,840,451,40))
        self.rfid.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.rfid.setFont(font4)
        self.rfid.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        self.rfid.setAlignment(Qt.AlignCenter)
        
        self.rfidRG = QPushButton(self.centralwidget)
        self.rfidRG.setObjectName(u"rfidRG")
        self.rfidRG.setGeometry(QRect(550, 840, 131, 41))
        self.rfidRG.setText(QCoreApplication.translate("MainWindow", u"GRAPH", None))
        self.rfidRG.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        
        self.btn_maximize = QPushButton(self.centralwidget)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(1223, 20, 17, 17))
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_minimize = QPushButton(self.centralwidget)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(1250, 20, 17, 17))
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.graphAIR = QPushButton(self.centralwidget)
        self.graphAIR.setObjectName(u"graphAIR")
        self.graphAIR.setGeometry(QRect(60, 350, 141, 31))
        self.graphAIR.setText(QCoreApplication.translate("MainWindow", u"GRAPH", None))
        self.graphAIR.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(85, 255, 127);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(105, 255, 150);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(55, 195, 95);\n"
        "}")
        
        self.graphTEMP = QPushButton(self.centralwidget)
        self.graphTEMP.setObjectName(u"graphTEMP")
        self.graphTEMP.setGeometry(QRect(310, 350, 141, 31))
        self.graphTEMP.setText(QCoreApplication.translate("MainWindow", u"GRAPH", None))
        self.graphTEMP.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(255, 0, 127);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 55, 155);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(199, 0, 99);\n"
        "}")
        
        self.graphHUM = QPushButton(self.centralwidget)
        self.graphHUM.setObjectName(u"graphHUM")
        self.graphHUM.setGeometry(QRect(560, 350, 141, 31))
        self.graphHUM.setText(QCoreApplication.translate("MainWindow", u"GRAPH", None))
        self.graphHUM.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(105, 200, 255);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(55, 130, 200);\n"
        "}")
        
        self.frontON = QPushButton(self.centralwidget)
        self.frontON.setObjectName(u"frontON")
        self.frontON.setGeometry(QRect(200, 430, 111, 41))
        # self.frontON.setText(QCoreApplication.translate("MainWindow", u"Button 1", None))
        self.frontON.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(105, 200, 255);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(55, 130, 200);\n"
        "}")
        
        self.frontOFF = QPushButton(self.centralwidget)
        self.frontOFF.setObjectName(u"frontOFF")
        self.frontOFF.setGeometry(QRect(200, 480, 111, 41))
        # self.frontON.setText(QCoreApplication.translate("MainWindow", u"Button 1", None))
        self.frontOFF.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(105, 200, 255);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(55, 130, 200);\n"
        "}")

        self.backON = QPushButton(self.centralwidget)
        self.backON.setObjectName(u"backON")
        self.backON.setGeometry(QRect(200, 530, 111, 41))
        # self.backON.setText(QCoreApplication.translate("MainWindow", u"Button 2", None))
        self.backON.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(85, 255, 127);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(105, 255, 150);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(55, 195, 95);\n"
        "}")

        self.backOFF = QPushButton(self.centralwidget)
        self.backOFF.setObjectName(u"backOFF")
        self.backOFF.setGeometry(QRect(200, 580, 111, 41))
        # self.backON.setText(QCoreApplication.translate("MainWindow", u"Button 2", None))
        self.backOFF.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(85, 255, 127);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(105, 255, 150);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(55, 195, 95);\n"
        "}")
        
        self.venON = QPushButton(self.centralwidget)
        self.venON.setObjectName(u"venON")
        self.venON.setGeometry(QRect(200,630,111,41))
        # self.venON.setText(QCoreApplication.translate("MainWindow", u"Button 3", None))
        self.venON.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(255, 0, 127);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 55, 155);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(199, 0, 99);\n"
        "}")
        
        self.venOFF = QPushButton(self.centralwidget)
        self.venOFF.setObjectName(u"venOFF")
        self.venOFF.setGeometry(QRect(200,680,111,41))
        # self.venON.setText(QCoreApplication.translate("MainWindow", u"Button 3", None))
        self.venOFF.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(255, 0, 127);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 55, 155);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(199, 0, 99);\n"
        "}")
        
        self.venOFF = QPushButton(self.centralwidget)
        self.venOFF.setObjectName(u"venOFF")
        self.venOFF.setGeometry(QRect(200,680,111,41))
        # self.venON.setText(QCoreApplication.translate("MainWindow", u"Button 3", None))
        self.venOFF.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(255, 0, 127);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 55, 155);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(199, 0, 99);\n"
        "}")
        
        self.allON = QPushButton(self.centralwidget)
        self.allON.setObjectName(u"allON")
        self.allON.setGeometry(QRect(200,730,111,41))
        # self.venON.setText(QCoreApplication.translate("MainWindow", u"Button 3", None))
        self.allON.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(254, 122, 1);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 122, 26);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(211, 76, 1);\n"
        "}")
        
        self.allOFF = QPushButton(self.centralwidget)
        self.allOFF.setObjectName(u"allOFF")
        self.allOFF.setGeometry(QRect(200,780,111,41))
        # self.venON.setText(QCoreApplication.translate("MainWindow", u"Button 3", None))
        self.allOFF.setStyleSheet(u"QPushButton {\n"
        "    background-color: rgb(254, 122, 1);\n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 122, 26);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(211, 76, 1);\n"
        "}")
        
        self.start = QLabel(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(810,140,67,17))
        self.start.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.start.setFont(font4)
        self.start.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.start.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.dateStart = QDateEdit(self.centralwidget)
        self.dateStart.setObjectName(u"dateStart")
        self.dateStart.setGeometry(QRect(890, 130, 101, 31))
        self.dateStart.setCalendarPopup(True)
        
        self.end = QLabel(self.centralwidget)
        self.end.setObjectName(u"end")
        self.end.setGeometry(QRect(1000,140,67,17))
        self.end.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.end.setFont(font4)
        self.end.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.end.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.dateEnd = QDateEdit(self.centralwidget)
        self.dateEnd.setObjectName(u"dateEnd")
        self.dateEnd.setGeometry(QRect(1080, 130, 101, 31))
        self.dateEnd.setCalendarPopup(True)
        
        self.min = QLabel(self.centralwidget)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(910,210,41,17))
        self.min.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.min.setFont(font4)
        self.min.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.min.setAlignment(Qt.AlignVCenter)
        
        self.max = QLabel(self.centralwidget)
        self.max.setObjectName(u"max")
        self.max.setGeometry(QRect(1000,210,41,17))
        self.max.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.max.setFont(font4)
        self.max.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.max.setAlignment(Qt.AlignVCenter)
        
        
        self.air = QLabel(self.centralwidget)
        self.air.setObjectName(u"air")
        self.air.setGeometry(QRect(810,250,67,17))
        self.air.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(11)
        self.air.setFont(font4)
        self.air.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.air.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.temperature = QLabel(self.centralwidget)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setGeometry(QRect(756,290,121,20))
        self.temperature.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(11)
        self.temperature.setFont(font4)
        self.temperature.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.temperature.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.humidity = QLabel(self.centralwidget)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setGeometry(QRect(796,330,81,20))
        self.humidity.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(11)
        self.humidity.setFont(font4)
        self.humidity.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.humidity.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.air_min = QLineEdit(self.centralwidget)
        self.air_min.setObjectName(u"air_min")
        self.air_min.setGeometry(QRect(900, 250, 51, 25))
        
        self.air_max = QLineEdit(self.centralwidget)
        self.air_max.setObjectName(u"air_max")
        self.air_max.setGeometry(QRect(1000, 250, 51, 25))
        
        self.temp_min = QLineEdit(self.centralwidget)
        self.temp_min.setObjectName(u"temp_min")
        self.temp_min.setGeometry(QRect(900, 290, 51, 25))
        
        self.temp_max = QLineEdit(self.centralwidget)
        self.temp_max.setObjectName(u"temp_max")
        self.temp_max.setGeometry(QRect(1000, 290, 51, 25))
        
        self.hum_min = QLineEdit(self.centralwidget)
        self.hum_min.setObjectName(u"hum_min")
        self.hum_min.setGeometry(QRect(900, 330, 51, 25))
        
        self.hum_max = QLineEdit(self.centralwidget)
        self.hum_max.setObjectName(u"hum_max")
        self.hum_max.setGeometry(QRect(1000, 330, 51, 25))
        
        self.airok_btn = QPushButton(self.centralwidget)
        self.airok_btn.setObjectName(u"airok_btn")
        self.airok_btn.setGeometry(QRect(1080, 250, 89, 25))
        
        self.tempok_btn = QPushButton(self.centralwidget)
        self.tempok_btn.setObjectName(u"tempok_btn")
        self.tempok_btn.setGeometry(QRect(1080, 290, 89, 25))
        
        self.humok_btn = QPushButton(self.centralwidget)
        self.humok_btn.setObjectName(u"humok_btn")
        self.humok_btn.setGeometry(QRect(1080, 330, 89, 25))
        
        self.search_btn = QPushButton(self.centralwidget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(1200, 130, 89, 221))
            
        self.time = QLabel(self.centralwidget)
        self.time.setObjectName(u"min")
        self.time.setGeometry(QRect(340,800,201,21))
        self.time.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.time.setFont(font4)
        self.time.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.time.setAlignment(Qt.AlignVCenter)
        
        self.labelFront = QLabel(self.centralwidget)
        self.labelFront.setObjectName(u"labelFront")
        self.labelFront.setGeometry(QRect(100,460,67,17))
        self.labelFront.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.labelFront.setFont(font4)
        self.labelFront.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.labelFront.setAlignment(Qt.AlignCenter)
        
        self.labelBack = QLabel(self.centralwidget)
        self.labelBack.setObjectName(u"labelBack")
        self.labelBack.setGeometry(QRect(100,560,67,17))
        self.labelBack.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.labelBack.setFont(font4)
        self.labelBack.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.labelBack.setAlignment(Qt.AlignCenter)
        
        self.labelVen = QLabel(self.centralwidget)
        self.labelVen.setObjectName(u"labelVen")
        self.labelVen.setGeometry(QRect(50,660,121,20))
        self.labelVen.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.labelVen.setFont(font4)
        self.labelVen.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.labelVen.setAlignment(Qt.AlignCenter)
        
        self.labelAll = QLabel(self.centralwidget)
        self.labelAll.setObjectName(u"labelAll")
        self.labelAll.setGeometry(QRect(110,760,51,20))
        self.labelAll.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.labelAll.setFont(font4)
        self.labelAll.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: transparent;\n"
"border-radius: 20px;")
        self.labelAll.setAlignment(Qt.AlignCenter)
        
        self.dbTable = QTableWidget(self.centralwidget)
        if (self.dbTable.columnCount() < 5):
            self.dbTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font6 = QFont()
        font6.setPointSize(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.dbTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.dbTable.setObjectName(u"dbTable")
        self.dbTable.setGeometry(QRect(780, 390, 501, 461))
        self.dbTable.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTEMP.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">TEMPERATURE</span></p></body></html>", None))
        self.labelDegreeTEMP.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">60</span><span style=\" font-size:40pt; vertical-align:super;\">°C</span></p>", None))
        # self.labelCredits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.labelHUM.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">HUMIDITY</span></p></body></html>", None))
        self.labelPercentageHUM.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">40</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        # self.labelCredits_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">60\u00ba</span></p></body></html>", None))
        self.labelAIR.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">AIR</span></p></body></html>", None))
        # self.labelCredits_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">20\u00ba</span></p></body></html>", None))
        self.labelPercentageAIR.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">25</span><span style=\" font-size:40pt; vertical-align:super;\">PPM</span></p>", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"The Best Switch In the World", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.rfid.setText(QCoreApplication.translate("MainWindow", u"RFID", None))
        self.rfidRG.setText(QCoreApplication.translate("MainWindow", u"Register", None))
#if QT_CONFIG(tooltip)

        self.labelFront.setText(QCoreApplication.translate("MainWindow", u"FRONT", None))
        self.labelBack.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.labelVen.setText(QCoreApplication.translate("MainWindow", u"VENTILATOR", None))
        self.labelAll.setText(QCoreApplication.translate("MainWindow", u"ALL", None))
        
        self.start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.end.setText(QCoreApplication.translate("MainWindow", u"END", None))
        self.dateStart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/mm/dd", None))
        self.dateEnd.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/mm/dd", None))
        self.min.setText(QCoreApplication.translate("MainWindow", u"MIN", None))
        self.max.setText(QCoreApplication.translate("MainWindow", u"MAX", None))
        self.air.setText(QCoreApplication.translate("MainWindow", u"AIR", None))
        self.temperature.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE", None))
        self.humidity.setText(QCoreApplication.translate("MainWindow", u"HUMIDITY", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        
        self.airok_btn.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.tempok_btn.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.humok_btn.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        
        self.air_min.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.air_max.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.temp_min.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.temp_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.hum_min.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.hum_max.setText(QCoreApplication.translate("MainWindow", u"100", None))
        
        ___qtablewidgetitem = self.dbTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.dbTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"AIR", None));
        ___qtablewidgetitem2 = self.dbTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE", None));
        ___qtablewidgetitem3 = self.dbTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"HUMIDITY", None));
        ___qtablewidgetitem4 = self.dbTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CREATE_AT", None));
        
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        
    # retranslateUi
        self.frontON.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.frontOFF.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.backON.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.backOFF.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.venON.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.venOFF.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.allON.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.allOFF.setText(QCoreApplication.translate("MainWindow", u"off", None))
        
        