from machine import Pin
from time import time, sleep
interval_time = 2
last_time = 0

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    buttonState = button.value()
    if buttonState == 1:
        last_time = time()
        led.value(1)
#         neu elif false thi led blink voi delay 0.2s
    elif (time() - last_time) > interval_time:
        led.value(not led.value())
        sleep(0.2)