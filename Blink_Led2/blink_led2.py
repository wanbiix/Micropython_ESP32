import time	#from time import sleep
import machine	 #from machine import Pin
led = machine.Pin(2, machine.Pin.OUT)	#led = Pin(2,Pin.OUT)		#Pin(2, Pin.OUT).value(0)
while True:
    led.on()		#led.value(not value())
    time.sleep(1)	# sleep(0.5)
    led.off()
    time.sleep(1)