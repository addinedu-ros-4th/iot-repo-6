import sys
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


# esp32 wifi setting
esp_32_ip = "192.168.0.12" 
esp_32_port = 80
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((esp_32_ip, esp_32_port))


# serial setting
ser = serial.Serial('/dev/ttyACM0', 9600)

from_class = uic.loadUiType("Qt.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("World class switch!!")
        self.count = 0
        
        self.time_values = []  # 시간 저장을 위한 리스트
        self.tem_values = []   # 온도 저장을 위한 리스트
        self.visualized_tem = False  


        # 카메라 설정
        self.pixmap = QPixmap()
        self.camera = Camera(self)
        self.camera.daemon = True   
        self.isCameraOn = False
        

        # 쓰레드 설정
        self.sensorThread = Sensor(client_socket)
        self.sensorThread.start()



        # 메소드 설정
        self.sensorThread.receive.connect(self.Recv)
        self.pushButton.clicked.connect(self.increase)
        self.pushButton2.clicked.connect(self.sendCommand)
        self.pushButton3.clicked.connect(self.visualizeTem)
        self.camera.update.connect(self.updateCamera)
        self.pushButton6.clicked.connect(self.clickCamera)



        # QTimer 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_count)
        self.timer.start(1000)  # 1초에 한 번씩 타이머가 작동



    def update_count(self):
        self.count += 1
        self.label2.setText(str(self.count))
        if self.count > 300:
            self.count = 0
            self.time_values = []
            self.tem_values = []

        

    def Recv(self, message):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.label4.setText(str(formatted_time))

        self.tem = str(message).split(',')[0].split('[')[1]
        self.label.setText(self.tem)

        self.hum = str(message).split(',')[1].split(']')[0]
        self.label3.setText(self.hum)
        

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



    def increase(self):
        self.count += 1
        self.label2.setText(str(self.count))

    
    def sendCommand(self):
        data_to_send = str(1)
        ser.write(data_to_send.encode())

    
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
        self.pixmap = self.pixmap.scaled(self.labelCamera.width(), self.labelCamera.height())
        self.labelCamera.setPixmap(self.pixmap)



    def clickCamera(self):
        if self.isCameraOn == False:
            self.pushButton6.setText("Camera off")
            self.isCameraOn = True
            
            self.camera.running = True      
            self.camera.start()                     # start() : run()을 실행시킴.
            self.video = cv2.VideoCapture(-1)       # 객체 생성 


        else:
            self.pushButton6.setText("Camera on")
            self.isCameraOn = False

            self.camera.running = False
            self.count = 0
            self.video.release()                    # 운영체제에 자원을 반환



class Sensor(QThread):
    receive = pyqtSignal(str)

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running =  True

    def run(self):
        try:
            while self.running:
                data = client_socket.recv(1024).decode()
                if len(data) > 0:
                    match = re.search(r'\[(.*?)\]', data)
                    if match:
                        json_data = f'[{match.group(1)}]'
                        self.receive.emit(str(json_data))
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
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())




