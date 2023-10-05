import network
from time import sleep
    
# def connectTo(ssid, password):
#     sta_if = network.WLAN(network.STA_IF)
#     if not sta_if.isconnected():
#         print('Connecting to network...')
#         sta_if.active(True)
#         sta_if.connect(ssid, password)
#         while not sta_if.isconnected():
#             pass
#     print('Network config:', sta_if.ifconfig())
# 
# connectTo("BK_University_GUEST", "")

ssid = 'LUN 1'
password = 'Xomtro179'

print("Connecting to WiFi network '{}'".format(ssid))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig())

print("Connecting to Blynk server...")