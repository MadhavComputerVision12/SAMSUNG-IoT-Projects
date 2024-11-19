from gpiozero import LED
from signal import pause

white = LED(2)

white.blink(1)
pause()
