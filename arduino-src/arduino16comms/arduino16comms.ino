#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN 650
#define SERVOMAX 2550
#define FREQUENCY 50

uint8_t servonum = 0;
int pos = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("16 channel servo test");

  pwm.begin();
  pwm.setPWMFreq(FREQUENCY);

  yield();
}

//Serial.read loop function
void loop() {
  if (Serial.available() > 0) {
    pos = Serial.parseInt();
    Serial.println(pos);
    int pulse_pos = map(pos, 0, 180, SERVOMIN, SERVOMAX);
    int analog_value_pos = int(float(pulse_pos) / 1000000 * FREQUENCY * 4096);
    pwm.setPWM(servonum,0,analog_value_pos);
  }
}
