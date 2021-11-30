import json
import pandas as pd
from operator import itemgetter

class Data:
    def __init__(self):
        with open('data/bottles.json', 'r') as j:
            json_bottles = json.load(j)
        # ID, Name, Volume
        self.bottles = json_bottles

        with open('data/boxes.json', 'r') as j:
            json_boxes = json.load(j)
        # ID, Name
        self.boxes = json_boxes

        # ID,Name,Ingredients,Volume,Boxes,Mix
        df = pd.read_csv('data/recipes.csv')
        self.df = df

        with open('data/queue.json', 'r') as j:
            json_queue = json.load(j)
        # ID, Name
        self.queue = json_queue

    def get_recipe(self, id):
        try: 
            num = list(self.df.ID).index(id)
            recipe = dict(zip((self.df.Ingredients[num]).split(','), (self.df.Volume[num]).split(',')))
            recipe = {'Name': self.df.Name[num], 'Ingredients': recipe, 'Boxes': (self.df.Boxes[num]).split(','), 'Mix': self.df.Mix[num]}
            return recipe # Ingredients(name, vol), Boxes, Mix
        except:
            print("ID not found")

    def add_recipe(self, name, ingredients, volume, boxes, mix):
        try:
            num = self.df.ID[len(self.df.ID)-1]+1
        except:
            num = 1
        dic = {'ID': num, 'Name': name, 'Ingredients': ingredients, 'Volume': volume, 'Boxes': boxes, 'Mix': mix}
        self.df = self.df.append(dic, ignore_index=True)
        self.df.to_csv('data/recipes.csv', index = False)

    def remove_recipe(self, id):
        try:
            self.df = self.df[self.df.ID != id]
            self.df.ID = list(range(1,self.df.shape[0]+1))
            self.df.to_csv('data/recipes.csv', index = False)
        except Exception as e:
            print(e)

    def change_bottle(self, num, name, volume):
        num = str(num)
        self.bottles[num] = [name, volume, self.bottles[num][2]]
        jsonFile = open("data/bottles.json", "w")
        jsonFile.write(json.dumps(self.bottles, indent=4, sort_keys=True))

    def change_box(self, num, name):
        num = str(num)
        self.boxes[num] = name
        jsonFile = open("data/boxes.json", "w")
        jsonFile.write(json.dumps(self.boxes, indent=4, sort_keys=True))

    def verify(self, id):
        num = list(self.df.ID).index(id)
        l = list(range(1,10))
        l.insert(1,10)
        diccsv = { 'Ingredients': str(self.df.Ingredients[num]).split(','),
                    'Volume': str(self.df.Volume[num]).split(','),}
        dicjson = { 'Ingredients': [x[0] for x in list(self.bottles.values())],
                    'Volume': [x[1] for x in list(self.bottles.values())]}
        dicjson['Calibrate'] = [0.035 for _ in list(range(1,11))]

        # For equal bottles
        for i in range(len(dicjson['Ingredients'])):
            for j in range(len(dicjson['Ingredients'])):
                if dicjson['Ingredients'][i] == dicjson['Ingredients'][j]:
                    dicjson['Ingredients'][i],dicjson['Ingredients'][j] = dicjson['Ingredients'][i] if (dicjson['Volume'][i] >= dicjson['Volume'][j]) else dicjson['Ingredients'][i]+'####', dicjson['Ingredients'][j] if (dicjson['Volume'][j] >= dicjson['Volume'][i]) else dicjson['Ingredients'][j]+'####'

        aux = {str(w):[x,y,z] for w,x,y,z in zip([str(x) for x in l],dicjson['Ingredients'], dicjson['Volume'], dicjson['Calibrate'])}

        # Is there enough?
        for i,j in zip(diccsv['Ingredients'],diccsv['Volume']):
            if i in dicjson['Ingredients']:
                if int(j)+50 > int(dicjson['Volume'][dicjson['Ingredients'].index(i)]):
                    return 'There is not enough '+ str(i), False
            else:
                return 'There is not enough '+ str(i), False

        dicjson = {str(w):[x,y,z] for w,x,y,z in zip([str(x) for x in l],dicjson['Ingredients'], dicjson['Volume'], dicjson['Calibrate'])}
        
        jsonFile = open("data/bottles.json", "w")
        jsonFile.write(json.dumps(dicjson, indent=4, sort_keys=True))
        
        return "Preparing "+self.df.Name[num]+"...", True

    def autocalibration(self, id):
        l = list(range(1,10))
        l.insert(1,10)
        num = list(self.df.ID).index(id)
        diccsv = { 'Ingredients': str(self.df.Ingredients[num]).split(','),
                    'Volume': str(self.df.Volume[num]).split(','),}
        dicjson = { 'Ingredients': [x[0] for x in list(self.bottles.values())],
                    'Volume': [x[1] for x in list(self.bottles.values())]}
        dicjson['Calibrate'] = [0.035 for _ in list(range(1,11))]
        for i,j in zip(diccsv['Ingredients'],diccsv['Volume']):
            dicjson['Volume'][dicjson['Ingredients'].index(i)] = str(int(dicjson['Volume'][dicjson['Ingredients'].index(i)]) - int(j))

        dicjson['Ingredients'] = [x.replace('####','') for x in dicjson['Ingredients']]
        
        dicjson = {str(w):[x,y,z] for w,x,y,z in zip([str(x) for x in l],dicjson['Ingredients'], dicjson['Volume'], dicjson['Calibrate'])}
        
        jsonFile = open("data/bottles.json", "w")
        jsonFile.write(json.dumps(dicjson, indent=4, sort_keys=True))
    
    def add_to_queue(self, id):
        n = str(len(self.queue.keys())+1)
        self.queue[n] = id
        jsonFile = open("data/queue.json", "w")
        jsonFile.write(json.dumps(self.queue, indent=4, sort_keys=True))

    def clean_queue(self):
        jsonFile = open("data/queue.json", "w")
        jsonFile.write(json.dumps({}, indent=4, sort_keys=True))

    def pause_queue(self, i):
        keys = [int(x) for x in self.queue.keys() if int(x) >= i]
        values = [self.queue[key] for key in [str(x) for x in keys]]
        self.queue = dict(zip([str(x) for x in range(1,len(keys)+1)], values))
        jsonFile = open("data/queue.json", "w")
        jsonFile.write(json.dumps(self.queue, indent=4, sort_keys=True))
