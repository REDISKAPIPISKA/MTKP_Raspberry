import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)

GPIO.setup(7, GPIO.IN)

print 'DETECTION SYSTEMS ACTIVATED!'

while True:
	if GPIO.input(7):
		GPIO.output(3,1)
	else:
		GPIO.output(3,0)
