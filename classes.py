import random
import copy
class Food: 
    """ RGO - Food currently includes all of the ingredients you might use to cook with, current thoughts and ideas relating are making a snack method that eats a small amount of a single type of food"""
    def __init__(self, food_type, servings):
        self.type = food_type
        self.servings = servings
        self.frozen = False 
        self.inedible_parts = 0 # not included in the serving size but assumed to be attached to the food until prepped
        # Determine the kcal_per_kg and expiration_time of a food
        if self.type == "Meat & Fish":
            self.inedible_parts = 0.1 # assumed
            self.kcal_per_g = random.gauss(2.24, 0.98)
            self.price_per_g = random.gauss(0.008, 0.0044)
            self.expiration_time = random.uniform(3, 11)
            self.g_per_serving = random.gauss(89, 51)
        elif self.type == "Dairy & Eggs":
            self.kcal_per_g = random.gauss(1.81, 1.1)
            self.price_per_g = random.gauss(0.00395, 0.0030)
            self.expiration_time = 7*random.uniform(1, 4)
            self.g_per_serving = random.gauss(109, 86)
        elif self.type == "Fruits & Vegetables":
            self.inedible_parts = 0.2 # assumed
            self.kcal_per_g = random.gauss(0.79, 0.73)
            self.price_per_g = random.gauss(0.00317, 0.0025)
            self.expiration_time = random.uniform(5.5, 14.5)
            self.g_per_serving = random.gauss(116, 63)
        elif self.type == "Dry Foods & Baked Goods":
            self.kcal_per_g = random.gauss(3.36, 1.23)
            self.price_per_g = random.gauss(0.00474, 0.0032)
            self.expiration_time = 7*random.uniform(1, 8)
            self.g_per_serving = random.gauss(65, 54)
        elif self.type == "Snacks, Condiments, Liquids, Oils, Grease, & Other":
            self.kcal_per_g = random.gauss(2.79, 1.99)
            self.price_per_g = random.gauss(0.00392, 0.0035)
            self.expiration_time = 30*random.uniform(3,18)
            self.g_per_serving = random.gauss(95, 79)
        elif self.type == 'Ready-to-eat':
            self.kcal_per_g = random.gauss(1.3, 2)
            self.price_per_g = random.gauss(0.005, 0.0035)
            self.expiration_time = random.uniform(4,11)
            self.g_per_serving = random.gauss(283, 75)
        else :
            raise ValueError("Not a listed Food Class")

    def decay(self):
        if self.frozen == False :
            self.expiration_time -= 1 # decays one day at a time

def CookedFood(Food):
    '''RGO - I am not a fan of the current attributes or more so that 
    it doesnt match regular foods, however this may be better'''
    def __init__(self, composition: dict, kg: float, kcal_per_kg: float):
        self.composition = composition
        self.type = 'Cooked, Prepared Items, & Leftovers'
        self.kg = kg
        self.kcal_per_kg = kcal_per_kg
        self.expiration_time = random.uniform(4, 11)
        

class Waste:
    def __init__(self, food_type: str, kg: float, inedible= False):
        self.type = food_type 
        self.amount_kg = kg 
        self.inedible = inedible

class Store:
    def __init__(self):
        self.shelves = []
        self.stock_shelves()
    
    def stock_shelves(self):
        food_types = [
        "Meat & Fish", 
        "Dairy & Eggs", 
        "Fruits & Vegetables", 
        "Dry Foods & Baked Goods", 
        "Snacks, Condiments, Liquids, Oils, Grease, & Other", 
        'Cooked, Prepared Items, & Leftovers' 
        ]
        # Can expand this to include different levels of freshness at the store to look at style of shopping on home fw like those who try to get the freshest produce
        for food_type in food_types: # add food to the store
            self.shelves.append(Food(food_type, servings=3)) # small package
            self.shelves.append(Food(food_type, servings=6)) # medium package
            self.shelves.append(Food(food_type, servings=10)) # big package

class House:
    def __init__(self, id, store: Store):
        self.id = id
        self.store = store
        self.members_adult = random.randint(1, 3) # income earning/providing members
        self.members_dependent = random.randint(0, 3) # Children and elderly
        # going based on servings and portions
        self.portion_size = 1 #assume all members eat a 1 serving portion each meal
        self.servings = self.portion_size*(self.members_adult+self.members_dependent)
        self.fridge = [] # stores the house's prepped meals
        self.pantry = [] # stores the house's ingerdients
        self.kitchen = [] # store the food that is in the process of being eaten or cooked
        self.waste_bin = [] # the house trashcan
        self.shopping_frequency = random.randint(1,7) #days between shopping trips
        self.shopping_quantity = 3*self.shopping_frequency # meals*days
        self.shopping_quantity *= self.members_adult+self.members_dependent # for all house members
        self.shopping_quantity += random.randint(0,3) # might often over shop
        self.time_available_for_meal_prep = [2, 0.5, 0.5, 0.5, 0.5, 0.5, 2] # unused currently

    def shop(self):
        # Randomly add some items to their pantry and fridge
        basket = 0
        while basket < self.shopping_quantity:
            item = random.choice(self.store.shelves)
            if item.type == 'Cooked, Prepared Items, & Leftovers':
                self.fridge.append(Food(item.type, item.servings))
            else :
                self.pantry.append(Food(item.type, item.servings))
            basket += item.servings
    
    def eat(self) :
        servings_left = self.servings 
        for food in self.fridge:
            # throws away bad food
            if food.expiration_time >= 0 :
                self.waste(food)
                
            # eat food unitl everyone is full currently assuming they eat a serving per meal
            elif servings_left > 0:
                if food.servings > servings_left:
                    food.servings -= servings_left
                else:
                    servings_left -= food.servings
                    self.fridge.remove(food)
                    del food
            else:
                break

    def waste(self, food: Food):
        self.waste_bin.append(Waste(food_type= food.type, kg= food.g_per_serving*food.servings/1000))
        self.fridge.remove(food)
        del food

    def prep(self, food: Food, servings_used: int):
        # create the food instance that is the prepped food
        prepped_food = copy.deepcopy(food)
        # if there is not enough servings we will currently assume that they just use what is there
        if servings_used >= food.servings:
            servings_used = food.servings
            self.pantry.remove(food)
            del food
        else:
            food.servings -= servings_used             
        if prepped_food.inedible_parts != 0:
            kg_inedible = servings_used * prepped_food.inedible_parts * prepped_food.g_per_serving/1000 # back calculates the amount of inedible waste
            inedible_waste = Waste(food_type= prepped_food.type, kg= kg_inedible, inedible= True) 
            self.waste_bin.append(inedible_waste)
            # give the prepped food the changed attributes
            prepped_food.inedible_parts = 0
            prepped_food.servings = servings_used
            # add the prepped food to the fridge
            self.kitchen.append(prepped_food)

    def cook(self): 
        ''' randomly selects some food and makes a meal out of it could use much work on how to selec the food to cook with'''
        servings_cooked = self.members_adult + self.members_dependent
        for i in range(random.randint(2,4)):
            self.prep(random.choice(self.pantry), servings_cooked)
            # End of selection
        composition = {}
        kg = 0
        kcal = 0
        for food in self.kitchen:
            if composition[food.type] not in composition:
                composition[food.type] = food.servings*food.g_per_serving/1000
            else:
                composition[food.type] += food.servings*food.g_per_serving/1000
            kg += food.servings*food.g_per_serving/1000
            kcal += food.servings*food.g_per_serving*food.kcal_per_g
            self.kitchen.remove(food)
            del food
        for key, value in composition:
            composition[key] = value/kg
        kcal_per_kg = kcal/kg
        meal = CookedFood()
        self.fridge.append(meal)    

    def check_pantry(self):
        for food in self.pantry:
            if food.expiration_time < 0:
                self.waste(food)