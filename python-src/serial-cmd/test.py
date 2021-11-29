import serial_cmd
import time

control = serial_cmd.Serial_cmd()

time.sleep(1.65)

for i in range(0, 4):
    num = '0'+str(i)
    control.set_servo(num, '050')
