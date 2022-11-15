
//Két LED fényerejének változtatása ellentétes irányben
// GD Szeged 2020 (ML)
int readValue = 0;
int writeValue1 = 0;
int writeValue2 = 0;
void setup() {
  pinMode(10, OUTPUT);            // LED 1 kimenet
  pinMode(11, OUTPUT);            // LED 2 kimenet
  Serial.begin(9600);
   }

 
void loop() {

  for (int i=0;i<255;i++)
  {
  writeValue1=i;//1-es LED fényerő
  writeValue2=255-i;//2-es LED fényerő
  Serial.print(" LED 1: ");// Szöveg és kettőspont kiíratása
  Serial.print(writeValue1);//Kápernyőre 1-es LED értéke
  analogWrite(10, writeValue1);     // írjuk ki az 1. LED-re
  analogWrite(11,writeValue2);    // írjuk ki az 2. LED-re
  Serial.print(" LED 2: ");//Szöveg és kettőspont kiíratása
  Serial.println(writeValue2); // kettes LED fényereje és soremelés
  delay (10); 
  }
  
  }
