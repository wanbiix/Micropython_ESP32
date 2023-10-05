from machine import ADC, Pin
from time import sleep, time

soil = ADC(Pin(32))
min_analog = 1590  # Replace with your value
max_analog = 4095  # Replace with your value
soil.atten(ADC.ATTN_11DB)
soil.width(ADC.WIDTH_12BIT)
total = 0
last_time = 0
while True:
    if (time() - last_time) > 1.5:
        current_analog = soil.read()
        for i in range(1000):
            total += current_analog
        moisture_per = ((total/1000 - min_analog) / (max_analog - min_analog)) * 100
        if moisture_per<0:
            moisture_per = 0 
        print('Moisture: ' f'{round((100-moisture_per), 1)} %') 
        total = 0
        last_time = time()

     
