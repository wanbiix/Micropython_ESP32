from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
  led.value(button.value())
  sleep(0.1)
