import cv2
import numpy as np
import serialmotorlist


class Motor_control:

    def __init__(self):
        self.num_columns = 4
        self.num_rows = 4
        self.num_motors = self.num_columns * self.num_rows
        self.motor_positions = [0] * self.num_motors

        self.column = 0
        self.row = 0
        self.target_motor = 0

        self.x = 0
        self.y = 0
        self.x_max = 400
        self.y_max = 300

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def wave_column():
        mod_iterator = 0
        while mod_iterator < 20:
            for i in range(self.num_motors):
                if i % self.num_columns == mod_iterator % self.num_columns:
                    self.motor_positions[i] = 180
                if i % self.num_columns == (mod_iterator + 1) % self.num_columns:
                    self.motor_positions[i] = 90
                if i % self.num_columns == (mod_iterator + 2) % self.num_columns:
                    self.motor_positions[i] = 0
                if i % self.num_columns == (mod_iterator + 3) % self.num_columns:
                    self.motor_positions[i] = 90
            print(self.motor_positions)
            # iterate movement to the next column
            mod_iterator += 1

    def motor_target(self):
        # based on the given postition of the body, determine the closest
        # motor in front of the person
        if self.x < self.x_max / self.num_columns:
            self.column = 0
            mod = 0
        elif self.x < 2 * (self.x_max / self.num_columns):
            self.column = 1
            mod = 1
        elif self.x < 3 * (self.x_max / self.num_columns):
            self.column = 2
            mod = 2
        else:
            self.column = 3
            mod = 3
        if self.y < self.y_max / self.num_rows:
            self.row = 0
        elif self.y < 2 * (self.y_max / self.num_rows):
            self.row = 1
        elif self.y < 3 * (self.y_max / self.num_rows):
            self.row = 2
        else:
            self.row = 3
        # convert the column and row of the motor to the motor number
        for i in range(self.num_motors):
            if i % self.num_columns == self.column:
                if self.row * self.num_rows <= i < (self.row + 1) * self.num_rows:
                    print(self.column)
                    print(self.row)
                    print(i)
                    self.target_motor = i

    def follow(self):
        # set the motor in front of the person and the surounding motors to
        # stick out
        self.motor_positions = [0] * self.num_motors
        self.motor_positions[self.target_motor] = 180
        if self.target_motor < 12:
            self.motor_positions[self.target_motor + self.num_columns] = 90
        if self.target_motor > 3:
            self.motor_positions[self.target_motor - self.num_columns] = 90
        if self.target_motor % self.num_columns != 0:
            self.motor_positions[self.target_motor - 1] = 90
        if self.target_motor % self.num_columns != 3:
            self.motor_positions[self.target_motor + 1] = 90
        
    def column_follow(self):
        pass

    def chaos(self, x, y):
        pass
