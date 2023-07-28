from logic.data import Data
from logic.control import Control

dat = Data()
# dat.add_recipe("Corange","Coconut,Orange,Milk","100,100,300","Lemon,Orange",False)

# rec = dat.get_recipe(1)
# print(type(rec['Ingredients']))

# dat.remove_recipe(1)

# dat.change_bottle(7,"Lemon",800)

# dat.change_box(5,"Gommy bears")

msg, ok = dat.verify(1)

print(msg)

# Process...

if ok:
    dat.autocalibration(1)
