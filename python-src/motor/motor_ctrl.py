class Motor_ctrl:

    def __init__(self):
        """Infrastructure for controlling grid of motors."""
        self.num_columns = 4
        self.num_rows = 4
        self.num_motors = self.num_columns * self.num_rows
        self.motor_positions = [0] * self.num_motors # List of all motor positions

        self.column = 0
        self.row = 0
        self.target_motor = 0 # Motor nearest target person

        # Position of target person
        self.x = 0
        self.y = 0
        self.x_max = 400
        self.y_max = 300

        print('Instantiated motor control class')

    def set_xy(self, x, y):
        """Sets coordinates of target person's position.

        Parameters:
            x (int): x-coordinate of target person.
            y (int): y-coordinate of target person.
        """
        self.x = abs(self.x_max - x)
        self.y = abs(self.y_max - y)

    def num_position(self, motor_num):
        """String formats the motor number and its position.

        Parameters:
            motor_num (int): motor number to be controlled.

        Returns:
            (tuple): contains string formatted motor number and position
        """
        pos = str(self.motor_positions[motor_num])
        if motor_num < 10:
            motor_num = '0' + str(motor_num)
        else:
            motor_num = str(motor_num)
        if len(pos) == 1:
            pos = '00' + pos
        elif len(pos) == 2:
            pos = '0' + pos
        return(motor_num, pos)

    def motor_target(self):
        """Sets target_motor to the motor closest to the position of the target person."""
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
                    self.target_motor = i

    def follow(self):
        """Sets the target and its surrounding motors to stick out."""
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

    def wave_column(self):
        """Insert description of movement here."""
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
            mod_iterator += 1 # Iterate movement to the next column

    def column_follow(self):
        for i in range(self.num_motors):
            if i % 4 == self.target_motor % 4:
                self.motor_positions[i] = 170
            else:
                self.motor_positions[i] = 0

    def chaos(self, x, y):
        pass
