import pandas as pd
import RPi.GPIO as GPIO
import time

class Control:
    def __init__(self):
        self.leds = [14,15,18,23,24,25,11] # Boxes and mixer
        self.pumps = [2,3,4,17,27,22,10,9] # Bottles
        self.vase = 26

        GPIO.setmode(GPIO.BCM)
        for i in (self.leds+self.pumps+[self.vase]): 
            GPIO.setup(i,GPIO.OUT)
            
    def pump_control(self, selected, seconds): #bottles
        for i,j in selected,seconds:
            GPIO.output(self.pumps.index(i-1), GPIO.HIGH)
            time.sleep(seconds)
            GPIO.output(self.pumps.index(i-1), GPIO.LOW)

    def led_control(self, selected): #boxes
        for i in selected:
            GPIO.output(self.leds.index(i-1), GPIO.HIGH)
        time.sleep(len(selected)*2)
        for i in selected:
            GPIO.output(self.leds.index(i), GPIO.HIGH)

    def vase_on(self):
        GPIO.output(self.vase, GPIO.HIGH)
    
    def vase_off(self):
        GPIO.output(self.vase, GPIO.LOW)
    
ctr = Control()
while(1):
    ctr.vase_on()
    time.sleep(1)
    ctr.vase_off()
    time.sleep(1)
