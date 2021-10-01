from apis.data import Data
from apis.control import Control

dat = Data()
# dat.add_recipe("Corange","Coconut,Orange,Milk","100,100,300","Lemon,Orange",False)
# dat.change_box("5","Ice")
# print(dat.verify(1))

# rec = dat.get_recipe(1)
# print(type(rec['Ingredients']))

# dat.add_recipe("Multivit", "Orange,Banana,Melon,Blueberry","100,150,200,200","Ice,Lemon,Coconut",True)

dat.remove_recipe(1)
dat.add_recipe("Corange","Coconut,Orange,Milk","100,100,300","Lemon,Orange",False)
dat.change_box("5","Ice")
msg, ok = dat.verify(1)

print(msg)

#TODO: Pumps and lights
if ok:
    dat.autocalibration(1)

