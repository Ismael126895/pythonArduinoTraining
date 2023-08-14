int potPin=A0;
int potVal;
int DL=100;
void setup() {
  Serial.begin(115200);
  pinMode(potPin,INPUT);
}

void loop() {
  potVal=analogRead(potPin);
  Serial.println(potVal);
  delay(DL);
}
