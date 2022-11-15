#include <Servo.h>                  // a szervo könyvtár
Servo myServo;                      // a szervo neve
 
// a használt kivezetések
const int onButtonPin = 2;
const int servoPin = 9;
int torlo_allas = 0;
void setup() 
{
  pinMode(onButtonPin,INPUT);
  myServo.attach(servoPin);
  
  // soros kommunikáció indítása
  Serial.begin(9600);
}


void loop() 
  {
  if (digitalRead(onButtonPin) == HIGH) // a nyomógombbal ki és bekapcsolunk
  {
    torlo_allas = torlo_allas + 1;
    if (torlo_allas >= 2) {torlo_allas = 0;}
  }  
  Serial.println(torlo_allas);// írassuk ki az állapotot
  delay (100);
  
  switch(torlo_allas) 
  {
  
    case 0:
      myServo.write(0);  // ha ki van kapcsolva, akkor 0 fokra álljon
    break;
    case 1:
      myServo.write(179);// ha be van kapcsolva, akkor töröljön
      delay(1000);
      myServo.write(0);
      delay(1000);
       break;
  }
}
