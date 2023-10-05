# https://www.youtube.com/watch?v=WM0unmRhojk

from hx711 import HX711
hx = HX711(dout = 5, pd_sck = 4)
# hx.set_scale(10)
xvar = 0
while True:
    hx.tare()
#     val = hx.get_units(10)
    read = hx.read()
    average = hx.read_average()
    
    
    print('\nLoop 5: ', read)
    
    print("Loop 40: ", average)

