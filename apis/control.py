import pandas as pd
import RPi.GPIO as GPIO
import time

class Control:
    def __init__(self):
        self.pumps = [2,3,4,17,27,22,10,9,11,0] # Bottles
        self.leds = [14,15,18,23,24,25] # Boxes and mixer
        self.mixer = 8

        GPIO.setmode(GPIO.BCM)
        [GPIO.setup(i,GPIO.OUT) for i in (self.leds+self.pumps+[self.mixer])]
        [GPIO.output(x, GPIO.HIGH) for x in self.pumps]
        GPIO.output(9, GPIO.LOW)
            
    def pump_control(self, selected, seconds, calibration): #bottles
        for i,j,k in zip(selected,seconds, calibration):
            GPIO.output(self.pumps[i], GPIO.LOW)
            time.sleep(float(j)*float(k))
            GPIO.output(self.pumps[i], GPIO.HIGH)

    def led_control(self, selected): #boxes
        for i in selected:
            GPIO.output(self.leds[i], GPIO.HIGH)
        time.sleep(len(selected)*2)
        for i in selected:
            GPIO.output(self.leds[i], GPIO.LOW)

    def mixer_on(self):
        GPIO.output(self.mixer, GPIO.HIGH)
    
    def mixer_off(self):
        GPIO.output(self.mixer, GPIO.LOW)
    
# ctr = Control()
# while(00):
#     ctr.mixer_on()
#     time.sleep(1)
#     ctr.mixer_off()
#     time.sleep(1)
