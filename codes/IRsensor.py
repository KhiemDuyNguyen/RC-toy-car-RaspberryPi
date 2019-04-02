from setupPins import *

class IRsensor():
    def __init__(self):
        self.state = False
    def update(self):
        sensor = GPIO.input(14)
        self.state = sensor
IRSENSOR = IRsensor()