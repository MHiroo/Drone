# sudo python3 /home/pi/Desktop/Drone/EscMoteurBrushless.py
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)

p.start(0)
print ("starting 0")
time.sleep(3)

p.ChangeDutyCycle(5)
print("start")
time.sleep(5)


i =5.5 
while i<7.5:
	
	print(i)
	p.ChangeDutyCycle(i)
	time.sleep(1)
	i += 0.1


