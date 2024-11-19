from gpiozero import LED

red = LED(21)
yellow = LED(20)
green = LED(16)

def red_blink():
	red.blink(1)
	pause(1)
def yellow_blink():
	yellow_blink(1)
	pause(1)
def green_blink():
	green_blink(1)
	pause(1)
def about_cpu():
	from gpiozero import LED
	import psutil
	from time import sleep
	from datetime import datetime

	led_yellow = LED(20)
	led_red = LED(21)
	file = open("/home/madhav12/Desktop/cpu_usage_log.txt","w")

	import psutil
	cpu_usage=psutil.cpu_percent(interval=1,percpu=True)
	print("Enter 1 to stop!")
	x=0

	while x!=1:
		x=int(input())
		cpu_usage=psutil.cpu_percent(interval=1,percpu=True)
		cpu_usage_mean=sum([i/len(cpu_usage) for i in cpu_usage])
		cpu_usage_mean=round(cpu_usage_mean,3)
		print(f"cpu usage(%) : {cpu_usage_mean}%")
		if 60>cpu_usage_mean>30: #usage over 30%
			led_yellow.on()
			led_red.off()
		elif cpu_usage_mean >= 60: #usage over 60%
			led_yellow.on()
			led_red.on()
		else:
			led_red.off()
			led_yellow.off()
			
		data = f"{datetime.now().strftime('%Y/%m/%d %HH %MM %SS')}"\
			f"cpu_usage(%) : {cpu_usage_mean}%\n"
		file.write(data)
		sleep(1)
	file.close()

	from datetime import datetime
	data=f"{datetime.now().strftime('%Y/%m/%d %HH %MM %SS')}"\
	f"cpu usage(%) : {cpu_usage_mean}%\n"

def partition():
	import psutil
	print(psutil.disk_partitions())
	print(psutil.disk_usage('/'))
	
def on_led_red():
	red.on()
def off_led_red():
	red.off()
def on_led_yellow():
	yellow.on()
def off_led_yellow():
	yellow.off()
def on_led_green():
	green.on()
def off_led_green():
	green.off()
def button():
		import RPi.GPIO as GPIO
		import time
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(26,GPIO.IN,pull_u_down=GPIO.PUD_UP)
		
		start_time=time.time()
		while time.time()-start_time<3:
			if GPIO.input(26)==GPIO.LOW: 
				print("YES! Button was pressed\n")
			else:
				print("NO! Button was not pressed\n")
def open_browser():
	import psutil
	import webbrowser
	import time
	before_cpu_usage=psutil.cpu_percent()
	print("CPU Utilisation before opening browser : ",before_cpu_usage,"%")
	
	webbrowser.open("https://www.google.com")
	
	time.sleep(10)
	
	after_cpu_usage=psutil.cpu_percent()
	print("CPU Utilisation after opening browser : ",after_cpu_usage,"%")
	
	
f = open('instruction.txt','r')
lines=f.readlines()


for line in lines:
	print(line)
	line=list(line.strip)
	if(line==["on" , "red" , "led"]):
		on_led_red()
	if(line==["on" , "yellow" , "led"]):
		on_led_yellow()
	if(line==["on" , "green" , "led"]):
		on_led_green()
	if(line==["off" , "green" ,"led"]):
		off_green_led()
	if(line==["off" , "yellow" , "led"]):
		off_yellow_led()
	if(line==["off" , "red" , "led"]):
		off_red_led()
	if(line==["blink" , "red" , "led"]):
		blink_red()
	if(line==["blink" , "yellow" , "led"]):
		blink_yellow()
	if(line==["blink" ,  "green" , "led"]):
		blink_green()
	if(line==["about" , "cpu"]):
		about_cpu()
	if(line==["partition"]):
		partition()
	if(line==["button"]):
		button()
	if(line==["open" , "browser"]):
		open_browser()
		
	else:
		print("Invalid Instruction")
		

