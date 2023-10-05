# Import required modules
import network
from machine import Pin
import BlynkLib
from time import sleep

# Connect to Wi-Fi network
ssid = "LUN 1"
password = "Xomtro179"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

print("Wi-Fi connected:", sta_if.ifconfig())

auth_token = "d8LC1LG_m7mNibJyl0Mi_YkTAONoLjPq"
blynk = BlynkLib.Blynk(auth_token)

led_pin = 2
led = Pin(led_pin, Pin.OUT)

# Define Blynk virtual pin handlers
@blynk.on("V0")
def v0_handler(value):
    if value[0] == 1:
        led.value(1)
    else:
        led.value(0)

# Start Blynk loop
while True:
    blynk.run()