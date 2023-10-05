import ntptime
import network
import utime
from time import sleep
from machine import I2C, Pin 
from i2c_lcd import I2cLcd 

AddressOfLcd = 0x27
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) # SCL=22, SDA=21
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('LUN 1', 'Xomtro179')

while not wifi.isconnected():
    try:
        pass
    except OSError as e:
        print("Lỗi khi kết nối WiFi:", e)
        
print("Connected to Wi-Fi")

# sử dụng ntptime để cập nhật thời gian từ máy chủ NTP
ntptime.host = "1.asia.pool.ntp.org"
ntptime.settime()


while True :
    utc_offset = 7 * 3600  # 7 giờ * 3600 giây/giờ
    current_time = utime.time() + utc_offset
    # Tính giờ, phút, giây từ thời gian đã được bù đắp
    hour = (current_time // 3600) % 24
    minute = (current_time % 3600) // 60
    second = current_time % 60
    print("Thời gian hiện tại: {}:{}:{}".format(hour, minute, second))
    lcd.move_to(0,0)
    lcd.putstr("{}:{}:{}".format(hour, minute, second))
    
    sleep(1)
    lcd.clear()


