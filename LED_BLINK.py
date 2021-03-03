import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

while True:

____GPIO.output(7, 1)

____time.sleep(1)

____GPIO.output(3, 0)

____time.sleep(1)
