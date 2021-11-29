#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN 650
#define SERVOMAX 2550
#define FREQUENCY 50

uint8_t servo_num = 0;
int servo_pos = 0;

void setup() {
  /* Starts serial communcation and assigns pins to servos. 
   */
  Serial.begin(115200); // start the serial port

  pwm.begin();
  pwm.setPWMFreq(FREQUENCY);
  yield();
}

void loop() {
  /* Reads incoming serial messages and sends them to the parseCommand function.
   */
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\r');
    parseCommand(command);
  }
}

void parseCommand(String command) {
  /* Parses incoming serial commands and executes corresponding response.
   * 
   * Parameters:
   *  command (String): the raw command sent over serial from Python.
   */  
  if (command.startsWith("M")) { // Command to set individual servo position
    servo_num = command.substring(1, 3).toInt(); 
    servo_pos = command.substring(3, 6).toInt();
    setServoPosition(servo_num, servo_pos);
    Serial.print(servo_num); Serial.print(","); 
    Serial.print(servo_pos); Serial.print(","); 
    Serial.println("R"); // Send received message
  } else {
    Serial.println("Error"); 
  }
}

bool setServoPosition(uint8_t num, int pos) {
    /* Set the given servo to the given position.
     * 
     * Parameters:
     *  num (16-bit int): the given servo number. 
     *  pos (int): the position to set the servo to. 
     * 
     * Returns:
     *  (bool): success of motor update
     */
    int pulse_pos = map(pos, 0, 180, SERVOMIN, SERVOMAX);
    int analog_value_pos = int(float(pulse_pos) / 1000000 * FREQUENCY * 4096);
    pwm.setPWM(num, 0, analog_value_pos);
    return true;
}
