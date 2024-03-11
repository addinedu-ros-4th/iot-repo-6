################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtGui import *

# GUI FILE
from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow

# GLOBALS
counter = 0
jumper = 10

## ==> YOUR APPLICATION WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.UiComponents()
        # self.labelCredits = QLabel(self)
        # self.labelCredits.setGeometry(1, 109, 30, 30)

        # # 이미지 파일 경로에 맞게 수정
        # self.labelCredits.setPixmap(QtGui.QPixmap("/home/addinedu/dev_ws/qt/switch2/temperature.png"))
        # self.isbtn_button1 = False
        # self.isbtn_button2 = False
        # self.isbtn_button3 = False
        
        # # btn_button 버튼 클릭 시 toggle_button 함수 호출
        # self.ui.btn_button1.clicked.connect(self.toggle_button1)
        # self.ui.btn_button2.clicked.connect(self.toggle_button2)
        # self.ui.btn_button3.clicked.connect(self.toggle_button3)
        
        # def toggle_button1(self):
        #     if not self.isbtn_button1:
        #         self.ui.btn_button1.setText("off")
        #         self.isbtn_button1 = True
        #     else:
        #         self.ui.btn_button1.setText("on")
        #         self.isbtn_button1 = False

        # # btn_button2를 토글하는 함수 정의
        # def toggle_button2(self):
        #     if not self.isbtn_button2:
        #         self.ui.btn_button2.setText("off")
        #         self.isbtn_button2 = True
        #     else:
        #         self.ui.btn_button2.setText("on")
        #         self.isbtn_button2 = False
        
        # def toggle_button3(self):
        #     if not self.isbtn_button3:
        #         self.ui.btn_button3.setText("off")
        #         self.isbtn_button3 = True
        #     else:
        #         self.ui.btn_button3.setText("on")
        #         self.isbtn_button3 = False        
    def UiComponents(self):
        mic_image_path = '/home/addinedu/dev_ws/qt/switch3/mic.png'
        # creating a push button
        self.btn_mic_button = QPushButton("", self)
    
        # setting geometry of button
        self.btn_mic_button.setGeometry(330, 750, 64, 64)
    
        # setting icon to the button
        self.btn_mic_button.setStyleSheet(f"QPushButton {{ background-image: url({mic_image_path}); background-repeat: no-repeat; }}")
            
        ## ==> SET VALUES TO DEF progressBarValue
        def setValue(self, slider, labelPercentage, progressBarName, color):

            # GET SLIDER VALUE
            # value = slider.value()

            # # CONVERT VALUE TO INT
            # sliderValue = int(value)

            # HTML TEXT PERCENTAGE
            htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
            # labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

            # CALL DEF progressBarValue
            # self.progressBarValue(sliderValue, progressBarName, color)

        ## ==> APPLY VALUES TO PROGREESBAR
        # self.ui.sliderTEMP.valueChanged.connect(lambda: setValue(self, self.ui.sliderTEMP, self.ui.labelDegreeTEMP, self.ui.circularProgressTEMP, "rgba(255, 0, 127, 255)"))
        # self.ui.sliderHUM.valueChanged.connect(lambda: setValue(self, self.ui.sliderHUM, self.ui.labelPercentageHUM, self.ui.circularProgressHUM, "rgba(85, 170, 255, 255)"))
        # self.ui.sliderAIR.valueChanged.connect(lambda: setValue(self, self.ui.sliderAIR, self.ui.labelPercentageRAM, self.ui.circularProgresAIR, "rgba(85, 255, 127, 255)"))

        # ## ==> DEF START VALUES
        # self.ui.sliderTEMP.setValue(25)
        # self.ui.sliderHUM.setValue(65)
        # self.ui.sliderAIR.setValue(45)

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)


## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)
        
        self.ui.setupUi(self)
        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())