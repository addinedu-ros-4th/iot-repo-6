#include <Servo.h>

int pushButton3 = 3;
int pushButton2 = 2;
bool flag = false;

Servo servo;
float pos = 0;

void setup() {
  Serial.begin(9600); 

  pinMode(pushButton3, INPUT);
  pinMode(pushButton2, INPUT);

  Serial.println("Hello. Ready!!!");
  servo.attach(9);
  servo.write(0);
}
//(단계별로 하나씩)
//1. 한번만 입력 받게 만들기

//2. 누르면 10도씩 증가

//3. 누르면 계속 동작

//4. -10도씩 움직이는 스위치 설치

void loop() {
  bool incomming_data3 = digitalRead(pushButton3);
  if (incomming_data3 == HIGH) {
    if (flag == false) {
      flag = true;
      Serial.println('1');
      pos = pos + 1;
      servo.write(pos);
    }
  }
  if (incomming_data3 == HIGH) {
    if (flag == true) {
      flag = false;
      // delay(30);
      }
    }

  else{
    if (flag == true) {
      flag = false;
      Serial.println('0');
      // servo.write(pos);
    }                        
  }

  bool incomming_data2 = digitalRead(pushButton2);
  if (incomming_data2 == HIGH) {
    if (flag == false) {
      flag = true;
      Serial.println('0');
      pos = pos - 1;
      servo.write(pos);
    }
  }
  if (incomming_data2 == HIGH) {
    if (flag == true) {
      flag = false;
      // delay(30);
      }
    }

  else{
    if (flag == true) {
      flag = false;
      Serial.println('0');
      servo.write(pos);
    }                                   
  }
}