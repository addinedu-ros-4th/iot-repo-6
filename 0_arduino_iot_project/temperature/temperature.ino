// #include <DHT.h>
// #include <DHT_U.h>
#include <IRremote.h>

#include <LiquidCrystal.h>  // 액정 디스플레이 라이브러리(아두이노 내장)

// 온습도 센서(DHT11) 라이브러리
// https://github.com/adafruit/DHT-sensor-library/blob/master/DHT.h
// #include "DHT.h"

// DHT11 초기화
// DHT dht(8, DHT11);

// 액정 디스플레이 초기화
// LiquidCrystal(rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  

const int RECV_PIN = A0;

IRrecv irrecv(RECV_PIN);
decode_results results;


void setup() {
  lcd.begin(16, 2);  // 16칸 2줄 LCD 디스플레이 사용
  irrecv.enableIRIn();
  Serial.begin(9600);  // 시리얼 통신 시작
}

void loop() {
  delay(2000);

  // 온습도 값 읽어들이기
  h = dht.readHumidity();
  t = dht.readTemperature();

  // 액정화면 표시
  lcd.setCursor(0, 0);
  lcd.print("Humi: "); lcd.print(h); lcd.print(" %");
  lcd.setCursor(0, 1);
  lcd.print("Temp: "); lcd.print(t); lcd.print(" C");

  // 시리얼 통신 표시
  Serial.print("{\"Humidity\": \""); Serial.print(h); Serial.print("\", ");
  Serial.print("\"Temperature\": \""); Serial.print(t); Serial.println("\"}");
}