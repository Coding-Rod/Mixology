import pandas as pd
import json

class Control:
    def __init__(self):
        self.leds = [0,1,2,3,4,5]
        self.pumps = [6,7,8,9,10,11]
        self.mixer = 12

    def pump_control(self, selected, time):
        # TODO: pump_control
        pass

    def led_control(self, selected):
        # TODO: led_control
        pass

    def mixer_control(self):
        # TODO: always ON
        pass
