
from gpiozero import LED, Button, MotionSensor, DistanceSensor

sensor = DistanceSensor(echo = 16, trigger = 15)#3rd is vcc
pir = MotionSensor(21)
off_button = Button(12)
red = LED(2)
green = LED(3)
white = LED(4)

password= input()

from gpiozero import MotionSensor,LED

import time
from time import sleep

password=input("Enter your password!: ")
print("Waiting for PIR to settle")
#pir.wait_for_no_motion()
time.sleep(3)
while True:
	print("Ready")
	pir.wait_for_motion()
	print("Motion Detected !")
	x=1
	while x==1:
			distance = sensor.distance * 100
			print("distance : ",distance)
			if distance<20:
				red.on()
				green.off()
				white.off()
				print("Enter password : ")
				pass=input()
				if(pass==password):
					print("How much time reactivate : ")
					v=int(input())
					sleep(v)
					print("Reactivated!")
				else:
					print("Wrong Password!")
			if distance<40:
				white.on()
				red.off()
				green.off()
			if distance<60:
				green.on()
				white.off()
				red.off()
			time.sleep(0.5)