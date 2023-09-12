# sudo python3 /home/pi/Desktop/Drone/ServoMoteurs2.py

from gpiozero import Servo
import time
import keyboard
from gpiozero.pins.pigpio import PiGPIOFactory

myGPIO = 17

maxPW = (2.35) / 1000
minPW = (1.0) / 1000

factory = PiGPIOFactory()

myServo = Servo(myGPIO, min_pulse_width=minPW, max_pulse_width=maxPW, pin_factory=factory)

print("Using GPIO17")
print("Max pulse width is set to 2.45 ms")
print("Min pulse width is set to 0.55 ms")

myServo.mid()
print("Set to middle position")

while True:
  
        if keyboard.is_pressed('q'):
            print("-90°")
            myServo.min()
            print("Set to minimum position")
            time.sleep(0.1)
        elif keyboard.is_pressed('s'):
            print("0°")
            myServo.mid()
            print("Set to middle position")
            time.sleep(0.1)
        elif keyboard.is_pressed('d'):
            print("+90°")
            myServo.max()
            print("Set to maximum position")
            time.sleep(0.1)
        elif keyboard.is_pressed('enter'):
            break
