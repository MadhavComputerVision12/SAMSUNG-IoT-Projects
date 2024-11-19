from gpiozero import Button, LED
from time import sleep
import random

led = LED(2)
player_1 = Button(21)
player_2 = Button(20)

while True:
	time = random.uniform(3,5)
	sleep(time)
	led.on()
	while True:
		if player_1.is_pressed:
			print("Player 1 wins")
			break
		if player_2.is_pressed:
			print("Player 2 wins")
			break
	led.off()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
