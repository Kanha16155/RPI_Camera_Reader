
int flash = 1;
int counter = 0;
int code[] = {000, 001, 010, 011, 100, 101, 110, 111};
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {


  if (code[counter] == 000)
  {
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  }
  else if (code[counter] == 001)
  {
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, HIGH);
  }
  else if (code[counter] == 010)
  {
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(10, LOW);
  }
  else if (code[counter] == 011)
  {
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  }
  else if (code[counter] == 100)
  {
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
  }
  else if (code[counter] == 101)
  {
    digitalWrite(12, HIGH);
    digitalWrite(11, LOW);
    digitalWrite(10, HIGH);
  }
  else if (code[counter] == 110)
  {
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, LOW);
  }
  else if (code[counter] == 111)
  {
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
  }

  delay(flash);
  Serial.println(counter);
  counter = counter + 1;
  if (counter == 8)
  {
    counter = 0;
  }
}
