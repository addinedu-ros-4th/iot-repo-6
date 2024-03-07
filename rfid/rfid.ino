#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop() {
  // 카드가 감지되면
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    // UID를 저장할 변수
    String cardUID = "";

    // UID를 시리얼 모니터에 출력하고 변수에 저장
    Serial.print("Card UID: ");
    for (byte i = 0; i < mfrc522.uid.size; i++) {
      Serial.print(mfrc522.uid.uidByte[i], HEX);
      Serial.print(" ");
      // UID를 문자열로 저장
      cardUID += String(mfrc522.uid.uidByte[i], HEX);
      cardUID.toUpperCase(); // 소문자를 대문자로 변경
      cardUID += " ";
    }
    Serial.println(); // 줄 바꿈

    // 시리얼 통신을 통해 UID를 파이썬으로 전송
    Serial.print("UID: ");
    Serial.println(cardUID);

    // 카드와의 통신 중지
    mfrc522.PICC_HaltA();
    mfrc522.PCD_StopCrypto1();

    // 잠시 대기
    delay(1000);

    // 다음 카드를 인식하도록 초기화
    mfrc522.PCD_Init();
  }
}






