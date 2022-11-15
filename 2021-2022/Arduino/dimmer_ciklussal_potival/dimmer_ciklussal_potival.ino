
int readValue = 0;
int writeValue1 = 0;
int writeValue2 = 0;
void setup() {
  pinMode(9, OUTPUT);             // LED 1 kimenet
  pinMode(10, OUTPUT);            // LED 1 kimenet
  pinMode(11, OUTPUT);            // LED 1 kimenet
  Serial.begin(9600);
   }

 
void loop() {

  readValue = analogRead(A0);     // tároljuk le a potenciométer állását
  Serial.print(" Poti : ");// Potm értéke
  Serial.print(readValue);//kiíratás új sorba
  writeValue1 = readValue/4;     // a kiírandó érték legyen a beolvasott érték negyede
  Serial.print(" LED 1: ");//kettőspont
  Serial.print(writeValue1);
  analogWrite(10, writeValue1);     // írjuk ki az 1. LED-re
  writeValue2 = 255 -writeValue1;
  analogWrite(11,writeValue2);    // írjuk ki az 1. LED-re
  Serial.print(" LED 2: ");//kettőspont
  Serial.println(writeValue2);
  delay (500);
  
  
  
  }
