const int sensor_Pin = A0;
int light = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  light = analogRead(sensor_Pin);
  Serial.println(light);
  delay(100);
  if (light > 500)
  {
    digitalWrite(2, HIGH);
    delay(1000);
    }
    if (light <= 50)
    {
       digitalWrite(2,LOW );
      }
      delay(100);
}
