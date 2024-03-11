int count = 0;


void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if ( count == 20 )
  {
    long value = Serial.parseInt();
    Serial.println(value);

    // All light Off (1)
    if ( value == 1 )
    {
      digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
      delay(500);                      // wait for a second
      digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    }
    count = 0;
  }
  count++;
}
