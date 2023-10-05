import ntptime
import network
import utime
from time import sleep

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('BK_University_GUEST', '')

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
    sleep(1)


