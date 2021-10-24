import json
import pandas as pd

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
        # print(self.df.Ingredients[0])

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
        num = self.df.ID[len(self.df.ID)-1]+1
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
        self.bottles[num] = [name, volume]
        jsonFile = open("data/bottles.json", "w")
        jsonFile.write(json.dumps(self.bottles, indent=4, sort_keys=True))

    def change_box(self, num, name):
        num = str(num)
        self.boxes[num] = name
        jsonFile = open("data/boxes.json", "w")
        jsonFile.write(json.dumps(self.boxes, indent=4, sort_keys=True))

    def verify(self, id):
        num = list(self.df.ID).index(id)
        # print(num)
        diccsv = { 'Ingredients': str(self.df.Ingredients[num]).split(','),
                    'Volume': str(self.df.Volume[num]).split(','),}
        dicjson = { 'Ingredients': [x[0] for x in list(self.bottles.values())],
                    'Volume': [x[1] for x in list(self.bottles.values())]}

        for i,j in zip(diccsv['Ingredients'],diccsv['Volume']):
            # print(i)
            # print(dicjson['Ingredients'])
            if i in dicjson['Ingredients']:
                if int(j) > int(dicjson['Volume'][dicjson['Ingredients'].index(i)]):
                    return 'Falta '+ str(i), False
            else:
                return 'Falta '+ str(i), False

        return "Preparando la bebida...", True

    def autocalibration(self, id):
        num = list(self.df.ID).index(id)
        diccsv = { 'Ingredients': str(self.df.Ingredients[num]).split(','),
                    'Volume': str(self.df.Volume[num]).split(','),}
        dicjson = { 'Ingredients': [x[0] for x in list(self.bottles.values())],
                    'Volume': [x[1] for x in list(self.bottles.values())]}

        for i,j in zip(diccsv['Ingredients'],diccsv['Volume']):
            dicjson['Volume'][dicjson['Ingredients'].index(i)] = str(int(dicjson['Volume'][dicjson['Ingredients'].index(i)]) - int(j))

        dicjson = dict(enumerate(zip(dicjson['Ingredients'],[int(x) for x in dicjson['Volume']]),1))
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
        i = int(i)
        keys = [int(x) for x in self.queue.keys() if int(x) >= i]
        values = list(self.queue.values())[len(keys)-1:]
        self.queue = dict(zip([str(x) for x in range(1,len(keys)+1)], values))
        jsonFile = open("data/queue.json", "w")
        jsonFile.write(json.dumps(self.queue, indent=4, sort_keys=True))

dat = Data()
dat.pause_queue(4)