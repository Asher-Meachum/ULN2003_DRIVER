# ULN2003 Driver
This project is a simple-to-use software driver that is written in Micropython. It is currently under active development. This project is designed solely to drive the ULN2003 motor driver, sensor feedback is out of scope for this project.

## Use the ULN2003 Driver
To use this driver, you can move the code file (`ULN2003_Driver.py`) into the project directory. It can then be imported like any other Python package.  
The driver has one method: `turn(direction, steps, delay)`.  
- `direction` has two possible values: `1` for clockwise rotation and `-1` for counterclockwise rotation.  
- `steps` determines the number of steps completed by the motor. It should be an positive integer. 
- `delay` determines the delay between each step. A larger delay will cause the motor to turn slower. The delay is currently capped on the lower end at 0.002, since a smaller delay will result in the motor vibrating without rotation.
## Limitations
This project currently has several limitations:  
- No sensor feedback. This feature is considered out of scope for this project.  
- No half steps. This feature is planned.  
- No concurrency. This feature is planned.

### Hardware
While this should work on any device running Micropython, I have only tested:  
- Raspberry Pi Pico (the original one) with the 28BYJ-48 Stepper Motor

## Contributing
This project welcomes contributions! Feel free to submit ideas for features, let me know of bugs, and contribute code.
### Project Structure
This project has several branches: `main`, `development`, `driver_testing`, and feature branches.  
`main` is the stable branch. Only urgent bug fixes should be committed directly to main, all other changes should be sent to development to be merged.  
`development` is stable, but may contain incomplete features. This is where most fixes or minor features should be merged to.  
`driver_testing` contains the tests required before being merged into `development`. It is preferred to test directly on the hardware, followed by Micropython on a desktop (shim layer is needed), followed by Python with shim layer. Pull Requests should note which test strategy was completed.  
`feature_name` branches are for major features (e.g. half step support). It is strongly recommended to discuss with the maintainers before opening a feature branch.