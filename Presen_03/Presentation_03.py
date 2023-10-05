import network
import BlynkLib
from time import sleep, time
from machine import Pin
import dht

def connectTo(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())
    
connectTo("LUN 1", "Xomtro179")
auth_token = "88YoD6E0Px5DjsGqT_n2UBsVZQNyeFtE"
blynk = BlynkLib.Blynk(auth_token)

cb_dht11 = dht.DHT11(Pin(33))
time_dht = 0
def get_dht():
    try:
        cb_dht11.measure()
        doC = cb_dht11.temperature()
        doam = cb_dht11.humidity()
        blynk.virtual_write(0, doC)
        blynk.virtual_write(1, doam)
        print('Nhiet do: %3.2f C' %doC + "    " + 'Do am: %3.2f %%' %doam)
    except OSError as e:
        print('Khong co gia tri tu cam bien.')

quat_pin = 22
quat = Pin(quat_pin, Pin.OUT)

@blynk.on('V2')  
def v2_read_handler(v2pin):
    quat.value(int(v2pin[0]))
#     if v2pin[0] == '1':
#         quat.value(1)
#     else:
#         quat.value(0)

while True:
    blynk.run()
    if (time() - time_dht) >= 1:
        get_dht()
        time_dht = time()
  