# ULN2003 Driver
This project is a simple-to-use software driver that is written in Micropython. It is currently under active development. This project is designed solely to drive the ULN2003 motor driver: sensor feedback is out of scope for this project.

## Use the ULN2003 Driver
To use this driver, download ULN2003_DRIVER.py, move into your project folder and import it into your project wiht `from ULN2003_Driver import ULN2003`. Initialise the motor driver with `ULN2003([motor1_pin1,motor1_pin2, motor1_pin3, motor1_pin4],[motor2_pin1,motor2_pin2, motor2_pin3, motor2_pin4],[motorx_pin1,motorx_pin2, motorx_pin3, motorx_pin4]])`. The motor is controlled via a method with the following arguments `turn(motor, direction, steps, delay)`. The direction argument is an integer input with 1 for clockwise and -1 for counterclockwise. The steps argument is an integer input which must be positive and will turn the motor the number of steps inputted. The delay argument controls the delay between steps and is set by default to 0.002. The library restricts the delay to a mininum of 0.002, since a lower value will cause the motor to vibrate and not turn.

## Limitations
This project currently has several limitations:
- No half steps. Support for this feature will be added in the (not too distant) future.
- No concurrency. Support for this feature will be added in the (more distant) future.

### Hardware
While this should work on any device running Micropython, I have only tested:
- Raspberry Pi Pico (the original one) with the 28BYJ-48 Stepper Motor

## Contributing
This project welcomes contributions! Feel free to submit ideas for features, let me know of bugs, and send me a pull requests.
### Project Structure
This project has several branches: main, development, driver_testing, and feature branches. main is the stable branch, and you should generally not try to commit to main. development is stable, but may contain incomplete features. This is where minor fixes should be merged to. driver_testing contains the testing file that I currently use for regression testing. If you are able to, please use it to test your code before submitting a pull request. Features that are being actively developed will get their own branch based off development.
