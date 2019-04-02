#camera module
from setupPins import *

class Camera():
    def __init__(self, angle):
        self.angle = angle
    def getCamAngle(self):
        return self.angle
    def setCamAngle(angle):
        self.angle = angle
        
    
CAMERA = Camera(dutyCycle) #neutral position