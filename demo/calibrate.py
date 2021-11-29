import RPi.GPIO as GPIO
import time

pin = int(input("Insert pin:\n"))

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while(1):
	calibrate_factor = float(input("Calibrate factor:\n"))
	GPIO.output(pin, GPIO.LOW)
	time.sleep(100*calibrate_factor)
	GPIO.output(pin, GPIO.HIGH)

GPIO.clenup()