from gpiozero import MotionSensor,LED

import time
led=LED(2)
pir = MotionSensor(21)
print("Waiting for PIR to settle")
#pir.wait_for_no_motion()
time.sleep(3)
while True:
	print("Ready")
	pir.wait_for_motion()
	print("Motion Detected !")
	led.on()
	time.sleep(1)
	led.off()
	time.sleep(1)
