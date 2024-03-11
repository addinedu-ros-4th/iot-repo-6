#include <DHT11.h>
#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN);
DHT11 dht11(A0);
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  pinMode(A1, INPUT);
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop() {
  // if (Serial.available() > 0) 
  // {
    int tem = 0;
    int hum = 0;
    int air = analogRead(A1);
    int result = dht11.readTemperatureHumidity(tem, hum);

    lcd.setCursor(0, 0);
    lcd.print("Hum");  lcd.print("  Tem "); lcd.print(" Air ");
    lcd.setCursor(0, 1);
    lcd.print(hum); lcd.print("%  "); lcd.print(tem); lcd.print("C  "); lcd.print(air); lcd.print("ppm"); 
    
    Serial.print("[");
    Serial.print(tem);
    Serial.print(",");
    Serial.print(hum);
    Serial.print(",");
    Serial.print(air);
    Serial.println("]");
    delay(100);
    
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) 
    {
      // UID를 저장할 변수
      String cardUID = "";

      // UID를 시리얼 모니터에 출력하고 변수에 저장
      // Serial.print("Card UID: ");
      for (byte i = 0; i < mfrc522.uid.size; i++) 
      {
        // Serial.print(mfrc522.uid.uidByte[i], HEX);
        // Serial.print(" ");
        // // UID를 문자열로 저장
        cardUID += String(mfrc522.uid.uidByte[i], HEX);
        cardUID.toUpperCase(); // 소문자를 대문자로 변경
        cardUID += " ";
      }
      // Serial.println(); // 줄 바꿈

      // 시리얼 통신을 통해 UID를 파이썬으로 전송
      Serial.print("{");
      Serial.print(cardUID);
      Serial.println("}");

      // 카드와의 통신 중지
      mfrc522.PICC_HaltA();
      mfrc522.PCD_StopCrypto1();

      // 잠시 대기
      delay(100);

      // 다음 카드를 인식하도록 초기화
      mfrc522.PCD_Init();
    }

  // }
}

