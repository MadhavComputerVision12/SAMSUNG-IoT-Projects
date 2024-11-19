from gpiozero import LED
from time import sleep

led={
"white" : LED(2),
"yellow":LED(3),
"red":LED(4)
}

while True:
	for i in led.keys():
		led[i].blink(on_time=1,off_time=1)
		sleep(2)
