#include <Servo.h>
#include <LiquidCrystal_I2C.h>

const int ledPin = 3;
const int ldrPin = A3;
Servo roofServo;

LiquidCrystal_I2C lcd(0x27,  16, 2);

int value;

void setup(){
  roofServo.attach(3);
  pinMode(ledPin, OUTPUT);  
  Serial.begin(9600);  
  lcd.init();
  lcd.backlight();

}

void loop(){
  
  value = analogRead(ldrPin); 
  Serial.println(value);
  
  if (value<=509){
    for (int angle=0;angle<360;angle++){
      roofServo.write(angle);
    }
    lcd.setCursor(0,0);
    lcd.print("ROOF OPEN");
  }
  else{
    for (int angle=360;angle>0;angle--){
      roofServo.write(angle);
    }
    lcd.setCursor(0,0);
    lcd.print("ROOF CLOSED");
  }
  delay(1000); 
}