from ULN2003_Driver_Dev import ULN2003
import random

motor = ULN2003(18,19,20,21)

try:
    motor.turn(1, 100)
    motor.turn(-1, 100)
    motor.turn(1, 100, 0.02)

    # Test ineligble inputs
    motor.turn(0, 100) # Invalid direction
    motor.turn(3, 100) # Invalid direction
    motor.turn(1, 0) # Invalid step number
    motor.turn(1, -4) # Invalid step number
except:
    print("Filtering test succeeded.")
finally:   
    # Random Tests
    for i in range(10):
        motor.turn(random.choice([-1,1]), random.randint(1,1000), random.randint(2,200)/1000)
