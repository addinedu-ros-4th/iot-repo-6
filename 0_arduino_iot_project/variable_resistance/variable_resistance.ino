const int LED = 9;

void setup ()
{
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop()
{
  int val = analogRead(A5)/4;
  Serial.println(val);
  analogWrite(LED, val);
}