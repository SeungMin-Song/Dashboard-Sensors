import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setwarning(False)

hallpin = 2

gpio.setup(hallpin, gpio.IN)

While True:
	if(gpio.input(hallpin) == False);
		print("magnet detected!, Sensor is working");
	else:
		print("magnet moves away.");