import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)

p.start(0)
print ("starting 0")
time.sleep(3)

p.ChangeDutyCycle(3)
print("start")
time.sleep(5)



while True:
	i = 5
	while i<7:
		
		print(i)
		p.ChangeDutyCycle(i)
		time.sleep(0.5)
		i +=.05
	
	
	while i>5:
		print(i)
		p.ChangeDutyCycle(i)
		time.sleep(0.5)
		i -=.05




