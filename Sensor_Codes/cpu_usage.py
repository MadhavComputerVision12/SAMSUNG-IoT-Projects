from gpiozero import LED
import psutil
from time import sleep
from datetime import datetime

led_yellow=LED(20)
led_red=LED(21)
file=open("/home/madhav12/Desktop/cpu_usage_log.txt","w")

