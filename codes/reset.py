from gpiozero import LED
from time import sleep

topR= LED(2)
botR = LED(3)
topL = LED(4)
botL = LED(8)

topR.on()
botR.on()
topL.on()
botL.on()