import RPi.GPIO as GPIO
import time

class Control:
    def __init__(self):
        self.pumps = [2,3,4,17,27,22,10,9,11,0] # Bottles

        GPIO.setmode(GPIO.BCM)
        [GPIO.setup(i,GPIO.OUT) for i in self.pumps]
        [GPIO.output(x, GPIO.HIGH) for x in self.pumps]
            
    def pump_control(self, selected, seconds, calibration): #bottles
        print(selected)
        try:
            print(8-selected[0])
        except:
            pass
        try:
            for i,j,k in zip(selected, seconds, calibration):
                GPIO.output(self.pumps[10-i], GPIO.LOW)
                time.sleep(float(j)*float(k))
                GPIO.output(self.pumps[10-i], GPIO.HIGH)
        except TypeError:
            GPIO.output(self.pumps[10-selected[0]], GPIO.LOW)
            time.sleep(float(seconds)*float(calibration[0]))
            GPIO.output(self.pumps[10-selected[0]], GPIO.HIGH)
