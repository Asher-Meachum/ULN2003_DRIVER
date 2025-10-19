"""
This is a Python library to be used as a compatability layer for running tests on the project.
It currently only supports the classes and method called in the dev branch, but you can send in a PR for other classes/methods you need.
It is intended for convenience, not as a substitue for testing in Micropython on actual hardware.
"""

def freq(frequency=None):
    return(None)

class Pin:
    IN = None
    OUT = None
    def __init__(self, pin_num: int, pin_mode):
        if pin_num < 0:
            raise ValueError("invalid pin")
    def value(self, value):
        return(None)