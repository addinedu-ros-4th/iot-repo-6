#include <WiFi.h>
#include <ESP32Servo.h>

const char* ssid = "AIE_509_2.4G";
const char* password = "addinedu_class1";
const int servoPin = 4;  // GPIO 4에 연결된 핀

Servo myServo;

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Wi-Fi에 연결 중...");
  }

  Serial.println("Wi-Fi에 연결됨");
  myServo.setPeriodHertz(50);  // 서보의 주기 설정
  myServo.attach(servoPin, 500, 2400);  // GPIO 4에 연결된 핀 설정 (추가)
  myServo.write(90);
  server.begin();
}

void handleCommand(String command) {
  if (command == "l") {
    myServo.write(myServo.read() - 60);
    Serial.println("왼쪽으로 30도 회전");
  } else if (command == "r") {
    myServo.write(myServo.read() + 60);
    Serial.println("오른쪽으로 30도 회전");
  } else {
    Serial.println("알 수 없는 명령");
  }
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("클라이언트 연결됨");
    while (client.connected()) {
      if (client.available()) {
        String command = client.readStringUntil('\n');
        command.trim();
        Serial.println("수신된 명령: " + command);

        // 수신된 명령을 처리하는 함수 호출
        handleCommand(command);

        client.println("명령 수신 및 처리 완료");
        break;
      }
    }
    client.stop();
    Serial.println("클라이언트 연결 해제됨");
  }
}




