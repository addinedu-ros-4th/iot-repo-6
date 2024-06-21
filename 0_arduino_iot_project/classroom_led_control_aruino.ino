// libray
#include <Servo.h>
#include <IRremote.h>

// IRremote setting
const int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;

// Servo setting
const int front_servo_pin = 9;
const int back_servo_pin = 8;
Servo front_servo;
Servo back_servo;

// delay setting
const int delay_time = 1;

// millis setting
const unsigned long interval = 100; // 0.1초
unsigned long previousMillis = 0;

// ange setting
const int front_on_angle = 0;
const int front_off_angle = 180;
const int back_on_angle = 0;
const int back_off_angle = 180;

void setup()
{
  Serial.begin(9600);
  front_servo.attach(front_servo_pin);
  front_servo.write(90);
  back_servo.attach(back_servo_pin);
  back_servo.write(90);
  irrecv.enableIRIn();
  Serial.println("connected");
}


void controlServo(int x) {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;
    if (x == 1) {
      front_servo.write(front_on_angle);
      delay(delay_time);
    }

    if (x == 2) {
      front_servo.write(front_off_angle);
      delay(delay_time);
    }

    if (x == 3) {
      back_servo.write(back_on_angle);
      delay(delay_time);
    }

    if (x == 4) {
      back_servo.write(back_off_angle);
      delay(delay_time);
    }
  }
}

void loop() {
  if (irrecv.decode(&results)) {
    switch (results.value) {
      case 0xFF30CF:
        // Serial.println("num_1 Front LED Turn on");
        controlServo(1);
        break;
      case 0xFF10EF:
        // Serial.println("num_4 Front LED Turn off");
        controlServo(2);
        break;
      case 0xFF18E7:
        // Serial.println("num_2 Back LED Turn on");
        controlServo(3);
        break;
      case 0xFF38C7:
        // Serial.println("num_5 Back LED Turn off");
        controlServo(4);
        break;
    }
    irrecv.resume();
  }
}
