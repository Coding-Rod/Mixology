import RPi.GPIO as GPIO
import time

class Control:
    def __init__(self):
        self.pumps = [2,3,4,17,27,22,10,9,11,0] # Bottles
        self.leds = [14,15,18,23,24,25] # Boxes and mixer

        GPIO.setmode(GPIO.BCM)
        [GPIO.setup(i,GPIO.OUT) for i in (self.leds+self.pumps)]
        [GPIO.output(x, GPIO.HIGH) for x in self.pumps]
            
    def pump_control(self, selected, seconds, calibration): #bottles
        print(selected)
        print(seconds)
        print(calibration)
        try:
            for i,j,k in zip(selected, seconds, calibration):
                GPIO.output(self.pumps[i], GPIO.LOW)
                time.sleep(float(j)*float(k))
                GPIO.output(self.pumps[i], GPIO.HIGH)
        except:
            GPIO.output(self.pumps[selected[0]], GPIO.LOW)
            time.sleep(float(seconds)*float(calibration[0]))
            GPIO.output(self.pumps[selected[0]], GPIO.HIGH)
