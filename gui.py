from apis.data import Data
from apis.control import Control

dat = Data()
dat.add_recipe("Corange","Coconut,Orange,Milk","100,100,300","Lemon,Orange",False)
dat.change_box("5","Ice")
msg, ok = dat.verify(1)

print(msg)

#TODO: Pumps and lights
if ok:
    dat.autocalibration(1)

