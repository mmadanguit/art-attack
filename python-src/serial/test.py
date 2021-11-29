import serial_cmd
from motor import motor_control
import time

control = serial_cmd.Serial_cmd()
time.sleep(1.65)
motor = motor_control.Motor_control()

for i in range(0, 10):
    motor.motor_positions = [150] * 16
    for i in range(0, 16):
        num, pos = motor.num_position(i)
        control.set_servo(num, pos)

    time.sleep(1)

    motor.motor_positions = [0] * 16
    for i in range(0, 16):
        num, pos = motor.num_position(i)
        control.set_servo(num, pos)

    time.sleep(1)


# for i in range(0, 4):
#     if i == 0:
#         x = 50
#         y = 50
#     if i == 1:
#         x = 360
#         y = 50
#     if i == 2:
#         x = 450
#         y = 450
#     if i == 3:
#         x = 250
#         y = 150
#     if i == 4:
#         x = 150
#         y = 250
# x = 250
# y = 20
# motor.set_xy(x, y)
# motor.motor_target()
# motor.follow()
# for i in range(0, 16):
#     # num = '0'+str(i)
#     num, pos = motor.num_position(i)
#     control.set_servo(num, pos)
