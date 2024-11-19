from gpiozero import LED

white = LED(2)

while True:
	white.on()
