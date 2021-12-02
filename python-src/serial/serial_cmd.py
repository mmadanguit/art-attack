import serial
import serial.tools.list_ports as list_ports
import string, array

class Serial_cmd:
    Arduino_IDs = ((0x2341, 0x0043), (0x2341, 0x0001),
                   (0x2A03, 0x0043), (0x2341, 0x0243),
                   (0x0403, 0x6001), (0x1A86, 0x7523))

    def __init__(self, port = ''):
        """Infrastructure for serial communication with the Arduino."""

        if port == '':
            self.dev = None
            self.connected = False
            devices = list_ports.comports()
            for device in devices:
                if (device.vid, device.pid) in Serial_cmd.Arduino_IDs:
                    try:
                        self.dev = serial.Serial(device.device, 115200)
                        self.connected = True
                        print('Connected to {!s}...'.format(device.device))
                    except:
                        pass
                if self.connected:
                    break
        else:
            try:
                self.dev = serial.Serial(port, 115200)
                self.connected = True
            except:
                self.dev = None
                self.connected = False

    def read(self):
        if self.connected:
            return self.dev.readline().decode()

    def write(self, command):
        """Sends data to the Arduino and waits for response.

        Parameters:
            command (str): command to be send over the Serial bus to the Arduino.
        """
        if self.connected:
            print('Called write')
            self.dev.write(f'{command}\r'.encode())
            print(f'{command}\r'.encode())
            print(self.read())
            return

    def set_servo(self, num, pos):
        """Sets individual servo position.

        Parameters:
            num (str): the given servo number.
            pos (str): the position to set the servo to.
        """
        if self.connected:
            print('Called set servo')
            command = f'M{num}{pos}'
            print(command)
            self.write(command)
