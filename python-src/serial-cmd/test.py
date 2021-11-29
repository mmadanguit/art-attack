import serial_cmd
import time
import position_to_motor

control = serial_cmd.Serial_cmd()
motor = position_to_motor.Motor_control()

time.sleep(1.65)


for i in range(0, 4):
    if i == 0:
        x = 50
        y = 50
    if i == 1:
        x = 360
        y = 50
    if i == 2:
        x = 450
        y = 450
    if i == 3:
        x = 250
        y = 150
    if i == 4:
        x = 150
        y = 250
    motor.set_xy(x, y)
    motor.motor_target()
    motor.follow()
    for i in range(0, 16):
        num = '0'+str(i)
        num, pos = motor.num_position(i)
        control.set_servo(num, pos)
