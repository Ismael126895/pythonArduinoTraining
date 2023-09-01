int potX=A1;
int potY=A0;
int potZ=2;
int dt=100;

int xVal=0;
int yVal=0;
int zVal=0;
void setup() {
  Serial.begin(115200);
  pinMode(potX,INPUT);
  pinMode(potY,INPUT);
  pinMode(potZ,INPUT);
  digitalWrite(potZ,HIGH);

}

void loop() {
  xVal=analogRead(potX);
  yVal=analogRead(potY);
  zVal=digitalRead(potZ);
  Serial.print(xVal);
  Serial.print(',');
  Serial.print(yVal);
  Serial.print(',');
  Serial.print(zVal);
  Serial.println(',');
  delay(dt);

}
