# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime
channel = 2
start_time = int(time.time())

while true
 GPIO.wait_for_edge(channel, GPIO.FALLING)
 print(int(time.time())




"""
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 

 
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)
 
   # message = raw_input('\nPress any key to exit.\n')
 
finally:
    GPIO.cleanup()
 
print("Goodbye!")
"""