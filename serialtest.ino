#include <Servo.h>

Servo servo1;
Servo servo2;
int servoPos;

void setup() {
  Serial.begin(9600); // start the serial port
  servo1.attach(10);
  servo2.attach(9);
}

void loop() {
  while (!Serial.available());
  servoPos = Serial.readString().toInt(); // get servo position from serial
  servo1.write(servoPos);
  delay(100);
  servo2.write(0);
}
