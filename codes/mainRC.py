#Main control
import rc
import setupPins

setupPins.reset()
car = rc.CAR

#Get character from keyboard to decide manual or self-driving mode

print("Press 'm' for manual mode, 'a' for self-driving, 'o' for voiding obstacles, the rest for quit")

c = setupPins.getch()
if(c == 'a' or c == 'A'):
    print("Self-driving mode")
    car.run("auto")
elif (c == 'm' or c == 'M'):
    print("Manual mode")
    car.run("manual")
elif (c == 'o' or c == 'Q'):
    print("Avoiding obstacle mode")
    car.run("obstacle")
