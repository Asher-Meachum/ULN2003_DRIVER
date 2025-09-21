from machine import Pin
from time import sleep

class ULN2003:
    def __init__(self, motor_pin_groups):
        try:
            self.motor_pin_groups = motor_pin_groups
            try:
                for i in len(motor_pin_groups):
                    if len(motor_pin_groups[i]) != 4:
                        motor_pin_groups[i] = []
                        raise TypeError(f"Initialisation expected four pin objects, but recieved a different number. Please check your arguments.")
            except TypeError:
                pass
            self.motors = [[Pin(pin_number, Pin.OUT) for pin_number in pin_group] for pin_group in self.motor_pin_groups]
        except ValueError:
            print("Invalid pins provided. Check the pinout of your microcontroller.")

        # Used to cycle through the pin combinations in clockwise & counterclockwise.
        self.drive_values = [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
    
    def turn(self, motor_id: int, direction: int, steps: int, delay: float = 0.002):
        if delay >= 0.002 and steps > 0:
            if direction == -1 or direction == 1:
                for step in range(steps):
                    i = 0
                    for i in range(4):
                        [pin.value(drive_val) for pin, drive_val in zip(self.motors[motor_id], self.drive_values)]
                        sleep(delay)
                        i+=direction
            else:
                raise ValueError("The value of direction is not valid. Please change the value to 1 (clockwise) or -1 (counterclockwise) to resolve this error.")
        else:
            if delay < 0.002:
                raise ValueError("The value of delay is smaller than 0.002. Please increase the value of delay to resolve this error.")
            if steps < 1:
                raise ValueError("The value of steps is smaller than 1. Please increase the value of steps to resolve this error.")
            [pin.value(0) for pin in self.motors[motor_id]]

