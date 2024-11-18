from gpiozero import LED
from signal import pause

white = LED(2)

while True:
	s = input()
	if (s=="on"):
		white.on()
	elif(s=="off"):
		white.off()
	elif(s=="blink"):
		white.blink(1)
		pause()
	else:
		print("invalid Command")
	
