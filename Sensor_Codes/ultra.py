from gpiozero import LED
from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=20, trigger=21)
led = LED(2)

while True:
	distance = sensor.distance * 100
	print("distance : ",distance)
	if distance<10:
		led.on()
	else:
		led.off()
	time.sleep(0.5)
