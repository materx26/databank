void setup() {
  // put your setup code here, to run once:
pinMode(3, OUTPUT);
pinMode(4, OUTPUT);
pinMode(5, OUTPUT);
pinMode(2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
for (int i = 0; i <= 5; i++)
{
for(int i = 0; i <= 10; i++)
{
  digitalWrite(3, HIGH);
  digitalWrite(5, LOW);
  delay(500);
  digitalWrite(3, LOW);
  digitalWrite(5, HIGH);
  delay(500);
  }
for(int i = 0; i <= 10; i++)
{
  digitalWrite(3, LOW);
  digitalWrite(5, LOW);
  digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(3, LOW);
  digitalWrite(5, LOW);
  digitalWrite(4, LOW);
  delay(500);
  }
  }
      for (int i = 0; i < 1500; i++)
    {
      digitalWrite(2, HIGH);
      delay(1);
      digitalWrite(2, LOW);
      delay(1);
      }
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);
    delay(10000);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);


    }
