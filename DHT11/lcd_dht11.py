from time import sleep
from machine import I2C, Pin 
from i2c_lcd import I2cLcd 
import dht
cb = dht.DHT11(Pin(33))

AddressOfLcd = 0x27
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) # SCL=22, SDA=21
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)

while True:
  try:
    sleep(1)
    cb.measure()
    nhiet_do = cb.temperature()
    do_am = cb.humidity()
    print('Temp: %3.1f C' %nhiet_do, "    ", 'Humi: %3.1f %%' %do_am)
    lcd.move_to(0,0) #Cột x hàng y
    lcd.putstr('T:%3.1fC' %nhiet_do)
    lcd.move_to(9,0) 
    lcd.putstr('H:%3.1f%%' %do_am)
  except OSError as e:
    print('Failed to read sensor.')