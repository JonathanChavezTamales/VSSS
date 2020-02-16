int pot;

void setup() {
  Serial.begin(115200);
  pinMode(36, INPUT);
}

void loop() {
  pot = analogRead(36);
  Serial.println(pot);
}
