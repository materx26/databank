#include <Servo.h>
Servo ms;
int potpin = A0;
int poti = 0;
int servopos = 0;
const int buttonpin = 2;
int last = 0;

int poses[10];
int mypose = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(buttonpin, INPUT);
ms.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
    poti = analogRead(potpin);
    servopos = map(poti, 0, 1023, 0, 179);
    ms.write(servopos);
    if (digitalRead(buttonpin) == HIGH)
    {
      if (mypose == 0)
      {
        poses[0] = servopos;
        mypose++;
        }
      if (poses[mypose++] == 0)
      {
        poses[mypose+1] = servopos;
        mypose++;
        }
      
    }
    delay(50);
    if (digitalRead(3) == HIGH)
    {
      Play();
      }
    
    
}
void Play()
{
  
      for (int i = 0; i < mypose; i++)
  {
    ms.write(poses[i]);
    delay(500);
    }
      
  }
