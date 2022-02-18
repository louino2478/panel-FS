void setup() {
  pinMode(5, INPUT); //bouton rouge // DRIVE
  pinMode(6, INPUT); //bouton jaune // RETURN
  pinMode(4, INPUT); //bouton gauche // speed+
  pinMode(3, INPUT); //bouton droit // speed-
  Serial.begin(9600);
}
void loop() {
  if(digitalRead(5) == true){ // DRIVE
    Serial.println("Drive");
    while(digitalRead(5) == true){
      delay(100);
      }
  }
  if(digitalRead(6) == true){ // RETURN
    Serial.println("Return");
    while(digitalRead(6) == true){
      delay(100);
      }
  }
  if(digitalRead(4) == true){ // speed+
    Serial.println("speedmore");
    while(digitalRead(4) == true){
      delay(100);
      }
  }
  if(digitalRead(3) == true){ // speed-
    Serial.println("speedless");
    while(digitalRead(3) == true){
      delay(100);
      }
  }
  if(Serial.available() > 0){ // pour tester la comunication
    delay(100);
    if(Serial.available() >= 4){
      if(Serial.read() == 112){ // verifie que "ping" est reçut (pas prope mais fonctionelle)
        if(Serial.read() == 105){
          if(Serial.read() == 110){
            if(Serial.read() == 103){
              Serial.println("pong"); // renvoie "pong"
            }
          }
        }
      }
    }
  }
  delay(15);
}
