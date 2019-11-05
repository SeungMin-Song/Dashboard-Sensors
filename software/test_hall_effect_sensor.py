import RPi.GPIO as GPIO

HALL = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(HALL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def change_detected(channel):
	if GPIO.input(HALL) == GPIO.LOW:
		print("Magnetic material detected.")
	else:
		print("No magnetic material.")

GPIO.add_event_detect(HALL, GPIO.BOTH, change_detected, bouncetime=25)

try:
	while True:
		pass

except KeyboardInterrup:
	print("Ctrl-C - quit")

finally:
	GPIO.cleanup()
