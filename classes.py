import random 
import copy
import pandas as pd

class Store():
    def __init__(self):
        self.shelves = pd.DataFrame(columns= [
            'Type', 
            'Servings', 
            'Expiration Min.', 
            'Expiration Max.',
            'Price',
            'kg',
            'kcal'
            ])
        self.stock_shelves()
    
    def stock_shelves(self):
        food_types = [
            "Meat & Fish", 
            "Dairy & Eggs", 
            "Fruits & Vegetables", 
            "Dry Foods & Baked Goods", 
            "Snacks, Condiments, Liquids, Oils, Grease, & Other", 
            'Store-Prepared Items' 
            ]
        for food_type in food_types:
            self.shelves[len(self.shelves)] = self.food_data(food_type=food_type, servings=3)
            self.shelves[len(self.shelves)] = self.food_data(food_type=food_type, servings=6)
            self.shelves[len(self.shelves)] = self.food_data(food_type=food_type, servings=10)

    def food_data(self, food_type: str, servings:int):
        ''' RGO - 
        Could make price smaller per kg for things with more 
        servings to improve accuracy to a real market'''
        inedible_parts = 0
        if food_type == 'Meat & Fish':
            exp_min = 4 # days 
            exp_max = 11 # days
            kg = 0.09*servings # assume 90g meat per serving
            price = 6*2.2*kg # assume $6/lb to total for kg
            kcal_kg = 2240 # assume 2240 kcal per kg of meat
            inedible_parts = 0.1
        elif food_type == 'Dairy & Eggs':
            exp_min = 7 # days 
            exp_max = 28 # days
            kg = 0.109*servings # assume 109g dairy&egg per serving
            price = 6*16/27*2.2*kg # assume $6/27oz to total for kg
            kcal_kg = 1810 # assume 1810 kcal per kg of dairy&eggs
            inedible_parts = 0.1
        elif food_type == 'Fruits & Vegetables':
            exp_min = 5 # days 
            exp_max = 15 # days
            kg = 0.116*servings # assume 116g f,v per serving
            price = 3.62*2.2*kg # assume $3.62/lb to total for kg
            kcal_kg = 790 # assume 790 kcal per kg of f,v
        elif food_type == 'Dry Foods & Baked Goods':
            exp_min = 7 # days 
            exp_max = 8*7 # days
            kg = 0.065*servings # assume 65g per serving
            price = 1.5*2.2*kg # assume $1.50/lb to total for kg
            kcal_kg = 3360 # assume 3360 kcal per kg
        elif food_type == 'Snacks, Condiments, Liquids, Oils, Grease, & Other':
            exp_min = 7 # days 
            exp_max = 8*7 # days
            kg = 0.095*servings # assume 95g per serving
            price = 3.3*2.2*kg # assume $3.30/lb to total for kg
            kcal_kg = 2790 # assume 2790 kcal per kg
        elif food_type == 'Store-Prepared Items':
            exp_min = 2 # days 
            exp_max = 7 # days
            kg = 0.095*servings # assume 95g per serving
            price = 0.33*16*2.2*kg # assume $0.33/oz to total for kg
            kcal_kg = 2790 # assume 2790 kcal per kg
        else:
            raise ValueError(f"{food_type}is not a listed Food Type")
        new_food = {
            'Type': food_type, 
            'Servings': servings, 
            'Expiration Min.': exp_min, 
            'Expiration Max.': exp_max,
            'Price': price,
            'kg': kg,
            'kcal_kg': kcal_kg,
            'Inedible Parts': inedible_parts
            }
        return new_food

    def buy(self,item_index:int):
        item_info = self.shelves.iloc[item_index].to_dict()
        return item_info

class Food():
    def __init__(self, food_data:dict ):
        self.type = food_data['Type']
        self.kg = food_data['kg']
        self.servings = food_data['Servings']
        self.expiration_time = random.randint(food_data['Expiration Min.'], food_data['Expiration Max.'])
        self.price_kg = food_data['Price']/kg
        self.inedible_parts = food_data['Inedible Parts']
        self.frozen = False
    def decay(self):
        if self.frozen == False:
            self.expiration_time -= 1

class CookedFood(Food):
    def __init__(self, composition: dict, kg: float, kcal_per_kg: float):
        self.composition = composition
        self.type = 'Cooked, Prepared Items, & Leftovers'
        self.kg = kg
        self.kcal_per_kg = kcal_per_kg
        self.expiration_time = random.uniform(4, 11)

class House():
    def __init__(self,id: int, store: Store):
        self.id = id
        self.store = store
        self.adults = random.randint(1,3)
        self.dependents = random.randint(0,2)
        self.kcal_day = self.adults*random.gauss(2144, 1308) + self.dependents*random.gauss(1800,1434)
        self.pantry = []
        self.fridge = []
        self.kitchen = []
        self.waste_bin = []
        self.shopping_frequency = random.randint(1,7) #days between shopping trips
    
