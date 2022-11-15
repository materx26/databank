int pos = 2;
int lasPos;
void setup() {
  // put your setup code here, to run once:
pinMode(3,OUTPUT); //pos0
pinMode(4,OUTPUT); //pos1
pinMode(5, OUTPUT); //pos2
pinMode(7, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(7) == HIGH)
  {
    for (int i=0; i<3; i++)
    {
      lasPos = pos;
      pos++;
      digitalWrite(pos, HIGH);
      digitalWrite(lasPos, LOW);
      delay(1000);
      }
      for (int i=3; i<1; i--)
      {
        lasPos = pos;
        pos--;
        digitalWrite(pos, HIGH);
        digitalWrite(lasPos, LOW);
        delay(1000);
        }
    }
  
}
