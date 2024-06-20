#include <ESP32Servo.h>
#include <WiFi.h>
#include <IRremote.h>

// remote setting
const int RECV_PIN = 25;
IRrecv irrecv(RECV_PIN);
decode_results results;

// wifi setting
const char* ssid = "AIE_509_2.4G";
const char* password = "addinedu_class1";
WiFiServer server(80);

// servo setting
const int leftServoPin = 4;
const int rightServoPin = 5;
const int fanServoPin = 14;
Servo leftServo;
Servo rightServo;
Servo fanServo;

// delay setting
const int delayTime = 200;

// angle setting
const int frontOnAngle = 145;
const int frontOffAngle = 40;
const int backOnAngle = 40;
const int backOffAngle = 145;
const int venOnAngle = 135;
const int venOffAngle = 45;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    // Serial.println("connected");
  }
  // Serial.println("connecting end");
  leftServo.setPeriodHertz(50);
  leftServo.attach(leftServoPin);
  leftServo.write(90);
  rightServo.setPeriodHertz(50);
  rightServo.attach(rightServoPin);
  rightServo.write(90);
  fanServo.setPeriodHertz(50);
  fanServo.attach(fanServoPin);
  fanServo.write(90);
  irrecv.enableIRIn();
  server.begin();
}

void controlServo(int x) {
  if (x == 1) {
    rightServo.write(frontOnAngle);
    delay(delayTime);
    rightServo.write(backOnAngle);
    delay(delayTime);
  }

  if (x == 2) {
    leftServo.write(frontOffAngle);
    delay(delayTime);
    leftServo.write(backOffAngle);
    delay(delayTime);
  }

  if (x == 3) {
    rightServo.write(frontOnAngle);
    delay(delayTime);
  }

  if (x == 4) {
    leftServo.write(frontOffAngle);
    delay(delayTime);
  }

  if (x == 5) {
    rightServo.write(backOnAngle);
    delay(delayTime);
  }

  if (x == 6) {
    leftServo.write(backOffAngle);
    delay(delayTime);
  }

  if (x == 7) {
    fanServo.write(venOnAngle);
    delay(delayTime);
  }

  if (x == 8) {
    fanServo.write(venOffAngle);
    delay(delayTime);
  }

  leftServo.write(90);
  rightServo.write(90);
  fanServo.write(90);
}

void processWifiCommand(String command) {
  if (command == "(turn all lights on)") {
    controlServo(1);
  }

  if (command == "(turn all lights off)") {
    controlServo(2);
  }

  if (command == "(turn front lights on)") {
    controlServo(3);
  }

  if (command == "(turn front lights off)") {
    controlServo(4);
  }

  if (command == "(turn back lights on)") {
    controlServo(5);
  }

  if (command == "(turn back lights off)") {
    controlServo(6);
  }

  if (command == "(turn ventilator on)") {
    controlServo(7);
  }

  if (command == "(turn ventilator off)") {
    controlServo(8);
  }
}

void loop() {
  // Check Wi-Fi command
  WiFiClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        String command = client.readStringUntil('\n');
        processWifiCommand(command);
      }
    }
  }

  // Check IR remote signal
  // (projection remote control_EIKI)
  if (irrecv.decode(&results)) {
    switch (results.value) {
      case 0xFDC1D3E0:
        // Serial.println("Up_button All LED Turn on");
        controlServo(1);
        break;
      case 0x32D36D68:
        // Serial.println("Down_button All LED Turn off");
        controlServo(2);
        break;
      case 0xFBA1C724:
        // Serial.println("Ok_button Front LED Turn off");
        controlServo(4);
        break;
      case 0xC347BF64:
        // Serial.println("Left_button Fan Turn on");
        controlServo(7);
        break;
      case 0x6D4D81E4:
        // Serial.println("Right_button Fan Turn off");
        controlServo(8);
        break;

        // (arduino remote control)
      case 0xFF30CF:
        Serial.println("num_1 All LED Turn on");
        controlServo(1);
        break;
      case 0xFF10EF:
        Serial.println("num_4 All LED Turn off");
        controlServo(2);
        break;
      case 0xFF18E7:
        Serial.println("num_2 Fan Turn on");
        controlServo(7);
        break;
      case 0xFF38C7:
        Serial.println("num_5 Fan Turn off");
        controlServo(8);
        break;
    }
    irrecv.resume();
  }
}
