from apis.data import Data

dat = Data()

dicjson = { 'Ingredients': [x[0] for x in list(dat.bottles.values())],
            'Volume': [x[1] for x in list(dat.bottles.values())]}

for i in range(len(dicjson['Ingredients'])):
    for j in range(len(dicjson['Ingredients'])):
        if dicjson['Ingredients'][i] == dicjson['Ingredients'][j]:
            dicjson['Ingredients'][i],dicjson['Ingredients'][j] = dicjson['Ingredients'][i] if (dicjson['Volume'][i] >= dicjson['Volume'][j]) else dicjson['Ingredients'][i]+'####', dicjson['Ingredients'][j] if (dicjson['Volume'][j] >= dicjson['Volume'][i]) else dicjson['Ingredients'][j]+'####'
            
print(dicjson)