import ntptime
from machine import RTC
import network

ssid = "LUN 1"
password = "Xomtro179"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

print('Network config:', sta_if.ifconfig())

# Synchronize with NTP server
ntptime.settime()

# Get UTC time
rtc = RTC()
(year, month, day, weekday, hour, minute, second, subsecond) = rtc.datetime()

# Add 7 hours for UTC+7
hour += 7
if hour >= 24:
    hour -= 24
    day += 1

print("Date (UTC+7): {}/{}/{} {}:{}:{}".format(day, month, year, hour, minute, second))