import dht
from machine import Pin
from time import sleep

cb = dht.DHT11(Pin(33))

while True:
  try:
    sleep(2)
    cb.measure()
    nhiet_do = cb.temperature()
    do_am = cb.humidity()
    
    print('Temp: %3.1f C' %nhiet_do + "    " + 'Humi: %3.1f %%' %do_am)
  except OSError as e:
    print('Failed to read sensor.')

