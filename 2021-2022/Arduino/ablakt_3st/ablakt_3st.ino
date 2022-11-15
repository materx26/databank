#include <Servo.h>                  // a szervo könyvtár
Servo mot; 
int state = 0;
int s0=11;
int s1=12;
int s2=13;

// a szervo neve mot(or)
 
// a használt kivezetések
const int servoPin = 3;

void setup() 
{
  mot.attach(servoPin);

  pinMode (s0, OUTPUT);
  pinMode (s1, OUTPUT) ;
  pinMode (s2, OUTPUT);
  attachInterrupt(0, blink, RISING);//megszakítás 2-es láb, negatív élre
  }

void loop()  
  
  
  {
switch(state) 
  {
    // ha ki van kapcsolva, akkor 0 fokra álljon
    case 0:
      digitalWrite (s0, HIGH);
      digitalWrite (s1, LOW);
      digitalWrite (s2, LOW);
        mot.write(0);
    break;
    case 1:
      digitalWrite (s0, LOW);
      digitalWrite (s1, HIGH);
      digitalWrite (s2, LOW);
        mot.write(179);
      delay(1000);
      mot.write(0);
      delay(1000);
       break;
  
       break;
      case 2:
      digitalWrite (s0, LOW);
      digitalWrite (s1, LOW);
      digitalWrite (s2, HIGH);
         mot.write(179);
      delay(4000);
      mot.write(0);
      delay(4000);
       break;
  
  
  }
  
  }
 
void blink()// a megszakítás után végrehajtandó
{
//állapot váltás
state = state + 1;
    if (state >= 3) {state = 0;}
  delay (500);
}
  
