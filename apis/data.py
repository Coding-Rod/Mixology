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

    def get_recipe(self, id):
        try: 
            num = list(self.df.ID).index(id)
            recipe = dict(zip((self.df.Ingredients[num]).split(','), (self.df.Volume[num]).split(',')))
            recipe = {'Ingredients': recipe, 'Boxes': (self.df.Boxes[num]).split(','), 'Mix': self.df.Mix[num]}
            return recipe # Ingredients(name, vol), Boxes, Mix
        except :
            print("ID not found")
            return None

    def add_recipe(self, name, Ingredients, volume, mix):
        # TODO: add_recipe
        pass

    def remove_recipe(self, name):
        try:
            self.df = self.df[self.df.Name != name]
            self.df.to_csv('data/recipes.csv', index = False)
        except Exception as e:
            print(e)

    def change_bottle(self, num, name, volume):
        # TODO:change_bottle
        pass

    def change_box(self, num, name):
        # TODO:change_box
        pass

# dat = Data()
# act_rec = dat.get_recipe(4)
# dat.remove_recipe("Corange")