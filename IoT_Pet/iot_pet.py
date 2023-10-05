import dht
from machine import Pin, ADC
from time import sleep, time

time_dht11 = 0
cb = dht.DHT11(Pin(33))

soil = ADC(Pin(32))
min_analog = 1590  
max_analog = 4095  
soil.atten(ADC.ATTN_11DB)
soil.width(ADC.WIDTH_12BIT)
time_doamdat = 0
total_doamdat = 0

def func_dht11():
    global time_dht11
    try:
        if (time() - time_dht11) > 2:
            cb.measure()
            nhiet_do = cb.temperature()
            do_am = cb.humidity()
            
            print('Temperature: %3.1f C' %nhiet_do, "   ", 'Humidity: %3.1f %%' %do_am)
            time_dht11 = time()
    except OSError as e:
        print('Khong co gia tri tra ve tu sensor.')
    
def func_doamdat():
    global time_doamdat, total_doamdat
    if (time() - time_doamdat) > 3:
        current_analog = soil.read()
        for i in range(1000):
            total_doamdat += current_analog
        moisture_per = ((total_doamdat/1000 - min_analog) / (max_analog - min_analog)) * 100
        if moisture_per<0:
            moisture_per = 0 
        print('Moisture: ' f'{round((100-moisture_per), 1)} %') 
        total_doamdat = 0
        time_doamdat = time()
        
while True:
    func_dht11()
    func_doamdat()

