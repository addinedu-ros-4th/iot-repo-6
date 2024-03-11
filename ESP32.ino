#include <DHT.h>
#include <WiFi.h>

const char* ssid = "AIE_509_2.4G";
const char* password = "addinedu_class1";
WiFiServer server(80);

DHT dht(5, DHT11);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    while (client.connected()) 
    {
      float tem = dht.readTemperature();
      float hum = dht.readHumidity();
      
      client.print("[");
      client.print(tem);
      client.print(",");
      client.print(hum);
      client.println("]");

      delay(200);  // 1초 대기 후 다시 센서 값을 보냄
    }

    client.stop();  // 클라이언트 연결이 끊기면 다시 대기 상태로 돌아감
  }
}
