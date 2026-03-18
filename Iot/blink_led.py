# 1초 간격으로 LED 불이 들어오고 나가는지 확인

import RPi.GPIO as GPIO
import time

is_pin_on = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)     # PIN_NUM, IO_TYPE(GPIO.OUT/GPIO.IN)
GPIO.output(4, GPIO.LOW)

try:
    while 1:
        if is_pin_on == 0:
            GPIO.output(4, GPIO.HIGH)   # 해당하는 핀의 전압을 높게
            is_pin_on = 1
        else: 
            GPIO.output(4, GPIO.LOW)
            is_pin_on = 0
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.output(4, GPIO.LOW)
    GPIO.cleanup()