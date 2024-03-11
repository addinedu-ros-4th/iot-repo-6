################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication
import socket
import time
from datetime import datetime
import re
import serial
import matplotlib.pyplot as plt
import cv2
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QGraphicsDropShadowEffect
import speech_recognition as sr


# GUI FILE
from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow

# GLOBALS
counter = 0
jumper = 10

# serial setting
ser = serial.Serial('/dev/ttyACM0', 9600)

## ==> YOUR APPLICATION WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.UiCAM()
        self.UiMIC()
        self.count = 0
        
        self.time_values = []  # 시간 저장을 위한 리스트
        self.tem_values = []   # 온도 저장을 위한 리스트
        self.visualized_tem = False  
        self.is_mic_listening = False  # 마이크 리스닝 상태를 나타내는 변수 추가

        # 카메라 설정
        self.pixmap = QPixmap()
        self.camera = Camera(self)
        self.camera.daemon = True   
        self.isCameraOn = False
        
        # 쓰레드 설정
        self.sensorThread = Sensor(ser)
        self.sensorThread.start()


        # 메소드 설정
        self.sensorThread.receive1.connect(self.Recv)
        self.sensorThread.receive2.connect(self.rfidRecv)
        # self.pushButton.clicked.connect(self.increase)
        # self.pushButton2.clicked.connect(self.sendCommand)
        self.ui.graphTEMP.clicked.connect(self.visualizeTem)
        self.camera.update.connect(self.updateCamera)
        self.btn_cam_button.clicked.connect(self.clickCamera)
        self.btn_mic_button.clicked.connect(self.clickMic)


        # QTimer 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_count)
        self.timer.start(1000)  # 1초에 한 번씩 타이머가 작동

    def update_count(self):
        if self.visualized_tem:
            self.count += 1
            # self.label2.setText(str(self.count))
            if self.count > 300:
                self.count = 0
                self.time_values = []
                self.tem_values = []

    def rfidRecv(self, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.ui.time.setText(str(formatted_time))

        try:
            self.rfid = str(message)
            # Assuming self.rfid is a QLabel or similar widget
            self.ui.rfid.setText(f"{self.rfid}님 환영합니다.")
        except Exception as e:
            print(f"Error in WifiManager: {e}")

    
    def Recv(self, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.ui.time.setText(str(formatted_time))

        self.tem = str(message).split(',')[0].split('[')[1]
        self.ui.labelDegreeTEMP.setText(f"{self.tem}°C")
    
        self.hum = str(message).split(',')[1]
        self.ui.labelPercentageHUM.setText(f"{self.hum}%")

        self.air = str(message).split(',')[2].split(']')[0]
        self.ui.labelPercentageAIR.setText(f"{self.air}PPM")

        if self.visualized_tem:
            self.time_values.append(self.count)
            self.tem_values.append(float(self.tem)) 

            if self.fig_tem is None:
                self.visualize()
            else:
                self.line_tem.set_xdata(self.time_values)
                self.line_tem.set_ydata(self.tem_values)
                self.ax_tem.relim()
                self.ax_tem.autoscale_view()
                self.fig_tem.canvas.flush_events()

    def visualizeTem(self):
        self.visualized_tem = True
        if self.visualized_tem:
            plt.ion()
            self.fig_tem, self.ax_tem = plt.subplots()
            plt.xlim([0, 300])
            plt.ylim([0, 100])
            self.line_tem, = self.ax_tem.plot(self.time_values, self.tem_values)
            self.ax_tem.legend()
            self.ax_tem.set_xlabel('Time')
            self.ax_tem.set_ylabel('Temperature (°C)')
            self.ax_tem.set_title('Real-time Temperature Visualization')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            self.fig_tem.canvas.mpl_connect('close_event', self.handle_close)

    def handle_close(self, event):
        if event.canvas.figure == self.fig_tem:
            self.visualized_tem = False
            self.fig_tem = None
            self.ax_tem = None
            self.line_tem = None
            self.time_values = []  
            self.tem_values = []  
            self.count = 0

    def closeEvent(self, event):
        if self.fig_tem is not None:
            self.visualized_tem = False
            self.fig_tem.canvas.mpl_disconnect(self.fig_tem.canvas.manager.key_press_handler_id)
            self.fig_tem.clear()
            plt.close(self.fig_tem)

    def updateCamera(self):
        retval, image = self.video.read()

        if retval:
            self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.original_image = self.image.copy()
            self.setImage()


    def setImage(self):
        h, w, c = self.image.shape
        qimage = QImage(self.image.data, w, h, w*c, QImage.Format_RGB888)
        self.pixmap = self.pixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.ui.camera.width(), self.ui.camera.height())
        self.ui.camera.setPixmap(self.pixmap)


    def clickCamera(self):
        if self.isCameraOn == False:
            # self.btn_cam_button.setText("Camera off")
            self.isCameraOn = True
            
            self.camera.running = True      
            self.camera.start()                     # start() : run()을 실행시킴.
            self.video = cv2.VideoCapture(-1)       # 객체 생성 


        else:
            # self.btn_cam_button.setText("Camera on")
            self.isCameraOn = False

            self.camera.running = False
            self.count = 0
            self.video.release()                    # 운영체제에 자원을 반환

    def clickMic(self):
        audio = None  # audio 변수를 초기화

        if not self.is_mic_listening:
            # 마이크에서 오디오 소스 생성
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("말해보세요!")  # 사용자에게 메시지 출력
                audio = r.listen(source)

            # 구글 웹 음성 API를 사용하여 음성 인식 (일일 50회 제한)
            try:
                recognized_text = r.recognize_google(audio, language='ko')
                print("Google 음성 인식이 인식한 내용: " + recognized_text)

                # 인식된 텍스트를 개별 문자로 리스트에 저장
                character_list = list(recognized_text)
                print("개별 문자:", character_list)

                # 리스트에서 특정 단어 확인 후 출력
                if "불" in character_list and "꺼" in character_list:
                    print("안녕하세요")
                    print(character_list)

            except sr.UnknownValueError:
                print("Google 음성 인식이 오디오를 이해하지 못했습니다.")
            except sr.RequestError as e:
                print("Google 음성 인식 서비스에서 결과를 요청할 수 없습니다; {0}".format(e))

        else:
            # 두 번째 클릭 시 음성 인식 멈추고 저장
            print("음성 인식 멈추고 저장")

            # 오디오를 WAV 파일로 저장
            if audio is not None:
                with open("microphone-results.wav", "wb") as f:
                    f.write(audio.get_wav_data())

        # 상태 변경
        self.is_mic_listening = not self.is_mic_listening


    
    def UiCAM(self):
        cam_image_path = '/home/ito/amr_ws/iot/project/iot-repo-6-jhr/switch3/camera.png'
        # creating a push button
        self.btn_cam_button = QPushButton("", self)
        # setting geometry of button
        self.btn_cam_button.setGeometry(610, 740, 64, 64)
        # setting icon to the button
        self.btn_cam_button.setStyleSheet(f"QPushButton {{ background-image: url({cam_image_path}); background-repeat: no-repeat; }}")

    def UiMIC(self):
        mic_image_path = '/home/ito/amr_ws/iot/project/iot-repo-6-jhr/switch3/mic.png'
        # creating a push button
        self.btn_mic_button = QPushButton("", self)
    
        # setting geometry of button
        self.btn_mic_button.setGeometry(330, 750, 64, 64)
    
        # setting icon to the button
        self.btn_mic_button.setStyleSheet(f"QPushButton {{ background-image: url({mic_image_path}); background-repeat: no-repeat; }}")
            
        ## ==> SET VALUES TO DEF progressBarValue
        def setValue(self, slider, labelPercentage, progressBarName, color):
            # HTML TEXT PERCENTAGE
            htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
            
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

class Sensor(QThread):
    receive1 = pyqtSignal(str)
    receive2 = pyqtSignal(str)

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running =  True

    def run(self):
        try:
            while self.running:
                data = ser.readline().decode().strip()
                if len(data) > 0:
                    match = re.search(r'\[(.*?)\]', data)
                    match2 = re.search(r'\{(.*?)\}', data)
                    if match:
                        json_data = f'[{match.group(1)}]'
                        self.receive1.emit(str(json_data))
                    
                    elif match2: 
                        json_data2 = f'[{match2.group(1)}]'
                        self.receive2.emit(str(json_data2))
                time.sleep(0.1)

        except Exception as e:
            print(f"Error in WifiManager: {e}")


class Camera(QThread):
    update = pyqtSignal()

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running =  True

    def run(self):
        count = 0
        while self.running == True:
            self.update.emit()          # 시그널을 발생시키는 함수.
            time.sleep(0.1)
    
    def stop(self):
        self.running = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())