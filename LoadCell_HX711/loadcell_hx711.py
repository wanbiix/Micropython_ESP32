from hx711 import HX711
hx = HX711(dout = 5, pd_sck = 4)
hx.set_scale(48.36)
hx.tare()
val = hx.get_units(10)
print(val)