#Manual mode for raspi-car
from setupPins import *

class manual():
    def run(self, camera):
        try:
            while True:
                p.ChangeDutyCycle(camera.getCamAngle())
                char = getch()
                if(char=="8"):
                    move_forward()
                    print("Fw")
                    sleep(0.03)
                elif(char=="2"):
                    move_backward()
                    print("Bw")
                    sleep(0.03)
                elif(char=="6"):
                    rotateCw()
                    print("CW")
                    sleep(0.03)
                elif(char=="4"):
                    rotateCcw()
                    print("CCW")
                    sleep(0.03)
                elif(char=="9"):
                    camera.angle-= 0.3
                    if(camera.angle <= 0):
                        camera.angle = 0
                    p.ChangeDutyCycle(camera.angle)
                    print("Camera: " + str(camera.angle))
                    sleep(0.01)
                elif(char=="7"):
                    camera.angle+= 0.3
                    if(camera.angle >= 12.5):
                        camera.angle = 12.5
                    p.ChangeDutyCycle(camera.angle)
                    print("Camera: " + str(camera.angle))
                    sleep(0.01)
                char = ""
                if char == "":
                    reset()
        except KeyboardInterrupt:
            GPIO.cleanup()
MANUAL = manual()
