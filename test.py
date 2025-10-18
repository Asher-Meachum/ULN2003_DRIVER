'''
This is the test script currently used before merging into dev branch.
It is divided into different functions based on purpose.
TODO: allow selecting of which tests to run for stable/dev branch
'''
from ULN2003_Driver import ULN2003
import random
import machine

motor = ULN2003([[18,19,20,21]])
frequency = machine.freq()
machine.freq(250000000)

# This function 
def correct_usage():
    motor.turn(0, 1, 100)
    motor.turn(0, -1, 100)
    motor.turn(0, 1, 100, 0.02)
    
def incorrect_usage():
    try:
        test_params = [[0,0,100, 0.002],[0,3,100,0.002],[0,1,0,0.002],[0,1,-4,0.002], [1,1,100,0.002],[-3,1,100,0.002]]
        for i in range(len(test_params)):
            motor.turn(test_params[i][0],test_params[i][1],test_params[i][2])
            print(f'Filtering test failed: {test_params[i]}')
            break
    except:
        pass

# TODO: add logic for handling both valid and invalid inputs
def random_correct_inputs():
    for i in range(10):
        param = [0,random.choice([-1,1]), random.randint(1,500), random.randint(2,20)/1000]
        print(f'{i}: {param}')
        motor.turn(param[0],param[1],param[2])
try:
    correct_usage()
    incorrect_usage()
    random_correct_inputs()
    print("All tests succeeded.")
finally:
    machine.freq(frequency)
