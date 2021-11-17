#include <Servo.h>

Servo servo1;
Servo servo2;
int servoPos;
int facialDist = 0;

String command = "";
bool hex2dec(char *str, uint16_t *val);



void setup() {
  Serial.begin(115200); // start the serial port
  
  servo1.attach(10);
  servo2.attach(9);
}

void loop() {
  if (Serial.available()) {
    char ch = Serial.read();

    if (ch == '\r') { // Check if command has been entered into Serial
      parse_command();
      command = "";
    } else {
      command += ch;
    }
  }

//  servoPos = map(facialDist, 0, 60, 0, 180); // Get servo position from facial distance
//  servo1.write(servoPos);
}



/*
** Parse commands sent from Serial.
*/
void parse_command() {
    uint16_t val;
    if (command.startsWith("DIST!")) {
      Serial.print("Received");
      if (hex2dec(command.substring(5), &val)) { 
        Serial.println(val);
        facialDist = val;
      }
    } 
}

/*
** Convert a string, str, into a 16-bit unsigned integer that is returned 
** using call by reference via val, skipping over any initial space or tab 
** characters. The function returns a boolean value that is true if the 
** conversion succeeded. The conversion is considered failed if there is 
** no valid sequence of hex digits or if the sequence of hex digits does 
** not end with the end of the string.
*/
bool hex2dec(String str, uint16_t *val) {
  uint8_t pos = 0;

  if (str.length() == 0)
    return false;

  while ((str.charAt(pos) == ' ') || (str.charAt(pos) == '\t')) {
    pos++;
  }

  *val = 0;
  while (pos < str.length()) {
    if ((str.charAt(pos) >= '0') && (str.charAt(pos) <= '9')) {
      *val = (*val << 4) + (str.charAt(pos) - '0');
    } else if ((str.charAt(pos) >= 'a') && (str.charAt(pos) <= 'f')) {
      *val = (*val << 4) + 10 + (str.charAt(pos) - 'a');
    } else if ((str.charAt(pos) >= 'A') && (str.charAt(pos) <= 'F')) {
      *val = (*val << 4) + 10 + (str.charAt(pos) - 'A');
    } else {
      return false;
    }
    pos++;
  }

  return true;
}
