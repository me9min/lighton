#include<Servo.h>
Servo myservo;
int sw = 8;
int pos = 0; 
int mortorPin = 12;
char input_data;

void setup() {
  myservo.attach(mortorPin);
Serial.begin(9600);
myservo.write(120); // init
  pinMode(sw, INPUT);     
}

boolean motorSwitch = true;
boolean tactSw = true;

void loop() {
  
 if (Serial.available() > 0){
    //정보가 있다면 변수 inByte 안에 저장
    input_data = Serial.read();
    //if() 사용
    //데이터가 A 바코드와 일치하는 경우 LED가 켜짐
    if (input_data == 'A'){
      Serial.print("A");
      motorSwitch = !motorSwitch;
    }
  }
  
  if(digitalRead(sw) == HIGH) {
    tactSw = true;
  }
  if(digitalRead(sw) == LOW && tactSw == true) {
    tactSw = false;
    motorSwitch  = !motorSwitch ;
    Serial.print("switch");
  }

  if(motorSwitch == true) {
     myservo.write(150); // on
  } else {
    myservo.write(70); // off
  }

  delay(100);
}
