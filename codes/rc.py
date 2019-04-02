from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep
import sys,tty,termios
import setupPins
import IRsensor
import manualMode
import autoMode
import obstacle
import camera

class rcCar:
    def __init__(self,  IRsensor, manual, auto, obstacle, camera, speed = 10.0, accel = 5.0, angle = 0.0):
        self.IRsensor = IRsensor
        self.manual = manual
        self.auto = auto
        self.obstacle = obstacle
        self.camera = camera
        self.brakeStatus = True
    def isIRSensor():
        return self.IRsensor.state()
    def run(self,mode):
        if (mode == "manual"):
            self.manual.run(self.camera)
        elif (mode == "auto"):
            self.auto.run()
        elif (mode == "obstacle"):
            self.obstacle.run()
    
CAR = rcCar(IRsensor.IRSENSOR, \
            manualMode.MANUAL, \
            autoMode.AUTO, \
            obstacle.OBSTACLE, \
            camera.CAMERA)



