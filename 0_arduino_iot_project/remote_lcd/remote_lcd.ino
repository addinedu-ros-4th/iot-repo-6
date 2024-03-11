/**
 * DHT11 Humidity Reader for Arduino
 * This sketch reads humidity data from the DHT11 sensor and prints the value to the serial port.
 * It also handles potential error states that might occur during reading.
 *
 * Author: Dhruba Saha
 * Version: 2.0.0
 * License: MIT
 */
#include <IRremote.h>

#include <LiquidCrystal.h>  // 액정 디스플레이 라이브러리(아두이노 내장)


// 액정 디스플레이 초기화
// LiquidCrystal(rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int RECV_PIN = A0; // 리모컨
IRrecv irrecv(RECV_PIN);
decode_results results;


void setup()
{
    lcd.begin(16, 2);  // 16칸 2줄 LCD 디스플레이 사용
    
    // Initialize serial communication to allow debugging and data readout.
    // Using a baud rate of 9600 bps.
    Serial.begin(9600);
    irrecv.enableIRIn();
}

void loop()
{
  if (irrecv.decode(&results)) 
  {
    // Serial.println(results.value, HEX); //16진수

    switch (results.value) {
      //num_0 Clear LCD panel
      case 0xFF6897:
      lcd.clear();
      Serial.print("num_0");
      break;
      //num_1 All LED Turn on"
      case 0xFF30CF:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_1"); Serial.println("num_1");
      lcd.setCursor(0, 1);
      lcd.print("All LED on");
      break;
      //num_2 All LED Turn off
      case 0xFF18E7:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_2"); Serial.println("num_2");
      lcd.setCursor(0, 1);      
      lcd.print("All LED off");
      break;
      //num_3 Front LED Turn on
      case 0xFF7A85:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_3"); Serial.println("num_3");
      lcd.setCursor(0, 1);
      lcd.print("Front LED on");
      break;
      //num_4 Front LED Turn off
      case 0xFF10EF:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_4"); Serial.println("num_4");
      lcd.setCursor(0, 1);
      lcd.print("Front LED off");
      break;
      //num_5 Back LED Turn on
      case 0xFF38C7:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_5"); Serial.println("num_5");
      lcd.setCursor(0, 1);     
      lcd.print("Back LED on");
      break;
      //num_6 Back LED Turn off
      case 0xFF5AA5:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_6"); Serial.println("num_6");
      lcd.setCursor(0, 1);
      lcd.print("Back LED off");
      break;
      //num_7 Fan Turn on
      case 0xFF42BD:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_7"); Serial.println("num_7");
      lcd.setCursor(0, 1);
      lcd.print("Fan on");
      break;
      //num_8 Fan Turn off
      case 0xFF4AB5:
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("num_8"); Serial.println("num_8");
      lcd.setCursor(0, 1);      
      lcd.print("Fan off");
      break;
    }
    irrecv.resume();
  }
}