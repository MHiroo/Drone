from gpiozero import Servo
from time import sleep

myGPIO=17

maxPW=(2.35)/1000
minPW=(1.0)/1000

myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

print("Using GPIO17")
print("Max pulse width is set to 2.45 ms")
print("Min pulse width is set to 0.55 ms")

while True:
  myServo.mid()
  print("Set to middle position")
  sleep(1)
  myServo.min()
  print("Set to minimum position")
  sleep(1)
  myServo.mid()
  print("Set to middle position")
  sleep(1)
  myServo.max()
  print("Set to maximum position")
  sleep(1)
