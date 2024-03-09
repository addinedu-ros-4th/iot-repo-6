#include <IRremote.h>

const int RECV_PIN = 11;
const int led1 = 7;


IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn();
  pinMode(led1, OUTPUT);
}

void loop() {
  if (irrecv.decode(&results)) 
  {
    Serial.println(results.value, HEX);

    // if(result.)

    switch (results.value) {
      case 0xFF30CF: digitalWrite(led1, HIGH);
      Serial.println("num_1 All LED Turn on");
      break;
      case 0xFF18E7: digitalWrite(led1, LOW); 
      Serial.println("num_2 All LED Turn off");      
      break;
      case 0xFF7A85: Serial.println("num_3 Front LED Turn on"); 
      break;
      case 0xFF10EF: Serial.println("num_4 Front LED Turn off"); 
      break;
      case 0xFF38C7: Serial.println("num_5 Back LED Turn on"); 
      break;
      case 0xFF5AA5: Serial.println("num_6 Back LED Turn off"); 
      break;
      case 0xFF42BD: Serial.println("num_7 Fan Turn on"); 
      break;
      case 0xFF4AB5: Serial.println("num_8 Fan Turn off"); 
      break;      
      // case 0xFF30CF: digitalWrite(led1, HIGH); break;
      // case 0xFF18E7: digitalWrite(led1, LOW); break;
      // case 0xFF30CF: digitalWrite(led1, HIGH); break;
      // case 0xFF18E7: digitalWrite(led1, LOW); break;


    }
    irrecv.resume();
  // Serial.println("All Turn on");
  }
}