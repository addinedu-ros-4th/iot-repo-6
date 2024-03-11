/**
 * DHT11 Humidity Reader for Arduino
 * This sketch reads humidity data from the DHT11 sensor and prints the value to the serial port.
 * It also handles potential error states that might occur during reading.
 *
 * Author: Dhruba Saha
 * Version: 2.0.0
 * License: MIT
 */

#include <LiquidCrystal.h>  // 액정 디스플레이 라이브러리(아두이노 내장)

// Include the DHT11 library for interfacing with the sensor.
#include <DHT11.h>

// Create an instance of the DHT11 class.
// - For Arduino: Connect the sensor to Digital I/O Pin 2.
// - For ESP32: Connect the sensor to pin GPIO2 or P2.
// - For ESP8266: Connect the sensor to GPIO2 or D4.
DHT11 dht11(8);

// 액정 디스플레이 초기화
// LiquidCrystal(rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int h;  // 습도
const int t;  // 온도


void setup()
{
    lcd.begin(16, 2);  // 16칸 2줄 LCD 디스플레이 사용
    
    // Initialize serial communication to allow debugging and data readout.
    // Using a baud rate of 9600 bps.
    Serial.begin(9600);
}

void loop()
{
    // Wait for 2 seconds before the next reading.
    delay(500);

    // 온습도 값 읽어들이기
    const int h = dht11.readHumidity();
    const int t = dht11.readTemperature();

    // 액정화면 표시
    lcd.setCursor(0, 0);
    lcd.print("Humi: "); lcd.print(h); lcd.print(" %");
    lcd.setCursor(0, 1);
    lcd.print("Temp: "); lcd.print(t); lcd.print(" C");

    // 시리얼 통신 표시
    Serial.print("{\"Humidity\": \""); Serial.print(h); Serial.print("\", ");
    Serial.print("\"Temperature\": \""); Serial.print(t); Serial.println("\"}");

}