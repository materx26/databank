
int readValue = 0;//potenciométer állása
int speed = 0;//változás sebessége
int writeValue2 = 0;
int valtozo=0;
void setup() {
  pinMode(9, OUTPUT);             // középső LED
  pinMode(10, OUTPUT);            // LED 1 kimenet
  pinMode(11, OUTPUT);            // LED 2 kimenet
  pinMode(12, OUTPUT);            // LED 3 kimenet
  pinMode(13, OUTPUT);            // LED 4 kimenet
  pinMode(2, INPUT);              //nyomógomb 2 bemenet
  Serial.begin(9600);
   }

 
void loop() {
  if (digitalRead(2)==LOW)
    {
    readValue = analogRead(A0);     // tároljuk le a potenciométer állását
    Serial.print(" Poti : ");// Potm értéke
    Serial.print(readValue);//kiíratás új sorba
    speed = readValue/4;     // a várakozási idő
    Serial.print(" LED 1: ");//kettőspont
    Serial.println(valtozo);
    analogWrite(9, valtozo);     // írjuk ki az 1. LED-re
    digitalWrite (10,HIGH);
    digitalWrite (11,HIGH);
    digitalWrite (12,HIGH);
    digitalWrite (13,HIGH);
    delay (speed);  
    digitalWrite (10,LOW);
    digitalWrite (11,LOW);
    digitalWrite (12,LOW);
    digitalWrite (13,LOW);
    delay (speed);
    digitalWrite (10,HIGH);
    digitalWrite (11,LOW);
    digitalWrite (12,HIGH);
    digitalWrite (13,LOW);
    delay (speed); 
    digitalWrite (10,LOW);
    digitalWrite (11,HIGH);
    digitalWrite (12,LOW);
    digitalWrite (13,HIGH);
    delay (speed);
    valtozo=valtozo+10;
  
    if (valtozo > 150)   //ha elértük a fényrő maximumot
    valtozo=0;   
    }
  else 
    {
    digitalWrite (10,LOW);
    digitalWrite (11,LOW);
    digitalWrite (12,LOW);
    digitalWrite (13,LOW);
    }
  }
