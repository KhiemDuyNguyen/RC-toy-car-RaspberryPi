#Setup GPIO
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep
import sys,tty,termios

def reset():
    topR.on()
    botR.on() 
    topL.on()
    botL.on()

servoPIN = 17
IRsensor = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(IRsensor,GPIO.IN)
sensor=GPIO.input(IRsensor)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(6) # Initialization
#dutyCycle
dutyCycle = 6
#p.ChangeDutyCycle(dutyCycle)

topR = LED(2)
botR = LED(3)
topL = LED(4)
botL = LED(8)

def move_forward():
    topR.off()
    topL.off()
def move_backward():
    botR.off()
    botL.off()
def rotateCw():
    topL.off()
    botR.off()
def rotateCcw():
    topR.off()
    botL.off()
def getch():
    fd = sys.stdin.fileno()
    old_settings= termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
    return ch




