##Program to send an email when motion is detected, Mark Poehlman, 11//2015
import time
import subprocess
import RPi.GPIO as GPIO
GPIO.setwarnings(False)##Disable Channel In Use Warnings
GPIO.setmode(GPIO.BOARD)##Use Board Pin Numbers
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) ##Board Pin 16, Connected to PIR Sensor
GPIO.setup(7,GPIO.OUT)##Pin 7 drives the LED or relay for alarm device
print("PIR2Mail Running...")
subprocess.call('date',shell=True)##Display date and time of program start on terminal
print("Waiting for PIR Sensor Event...")
while True:
	if(GPIO.input(16) ==1):  ##If PIR Sensor goes high
		GPIO.output(7,True)##Turn LED or Alarm on
		print("---------------------------------------------------------------------")
		subprocess.call('date',shell=True)##Display date and time of PIR Sensor event on terminal
		print("Motion Detected by PIR Sensor on Pin 16, Sending Email")##Display message on terminal
		##Send an email 
		subprocess.call('echo "Motion Detected by PIR Sensor on Pin 16" | mail -s "Motion Detected by Python" recipient.email.address',shell=True)	
		print("Email Sent")
		print("LED is On, Begin 60 Second Delay...")
		time.sleep(60) ##Pause for 60 seconds to eliminate repeated alarms
		print("60 Second Delay Complete, LED is Off")
		GPIO.output(7,False)##Turn LED or Alarm off
		print("Waiting for PIR Sensor Event...") 
GPIO.cleanup()
