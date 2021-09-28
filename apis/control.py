import pandas as pd
import json
from data import Data

class Control:
    def __init__(self):
        self.dat = Data()
        self.leds = [0,1,2,3,4,5]
        self.pumps = [6,7,8,9,10,11]
        self.mixer = 12

    def verify(self, id):
        # TODO: Verify if resources are available for recipe
        pass

    def pump_control(self, selected):
        # TODO: pump_control
        pass

    def led_control(self, selected):
        # TODO: led_control
        pass

    def mixer_control(self):
        # TODO: always ON
        pass
