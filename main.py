import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Food:
    def __init__(self, food_type, servings):
        self.type = food_type
        self.servings = servings
        self.frozen = False 
        # Determine the kcal_per_kg and expiration_time of a food
        if self.type == "Meat & Fish":
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
        elif self.type == 'Cooked, Prepared Items, & Leftovers':
            self.kcal_per_g = random.gauss(1.3, 2)
            self.price_per_g = random.gauss(0.005, 0.0035)
            self.expiration_time = random.uniform(4,11)
            self.g_per_serving = random.gauss(283, 75)
        else :
            raise ValueError("Not a listed Food Class")

    def decay(self):
        if self.frozen == False :
            self.expiration_time -= 1 # decays one day at a time


class Waste:
    def __init__(self, food: Food, day):
        self.type = food.type 
        self.amount_kg = food.g_per_serving*food.servings/1000 #g/kg
        self.day_wasted = day 


class House:
    def __init__(self, id):
        self.id = id
        self.members_adult = random.randint(1, 3) # income earning/providing members
        self.members_dependent = random.randint(0, 3) # Children and elderly
        # going based on servings and portions
        self.portion_size = 1 #assume all members eat a 1 serving portion each meal
        self.servings = self.portion_size*(self.members_adult+self.members_dependent)
        self.menu = [] # stores all of a households foods
        self.waste_bin = [] # the house trashcan
        self.shopping_frequency = random.randint(1,7) #days between shopping trips
        self.shopping_quantity = 3*self.shopping_frequency # meals*days
        self.shopping_quantity *= self.members_adult+self.members_dependent # for all house members
        self.shopping_quantity += random.randint(0,3) # might often over shop

    def shop(self):
        # Randomly add some items to their menu
        basket = 0
        while basket < self.shopping_quantity:
            item = random.choice(store)
            self.menu.append(Food(item.type, item.servings))
            basket += item.servings
    
    def eat(self) :
        random.shuffle(self.menu)
        servings_left = self.servings 

        for food in self.menu:
            # throws away bad food
            if food.expiration_time >= 0 :
                self.waste(food)
            elif servings_left > 0:
                if food.servings > servings_left:
                    food.servings -= servings_left
                else:
                    servings_left -= food.servings
                    self.menu.remove(food)
                    del food
            else:
                break

    def waste(self, food: Food):
        self.waste_bin.append(Waste(food, day=None))
        self.menu.remove(food)
        del food 

def setup():
    global days 
    days = 100 
    global store 
    store = [] # the place people go to buy groceries
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
        store.append(Food(food_type, servings=3)) # small package
        store.append(Food(food_type, servings=6)) # medium package
        store.append(Food(food_type, servings=10)) # big package
    global houses 
    houses = [] # stores houses
    num_of_houses = 2
    for i in range(num_of_houses):
        house = House(i)
        houses.append(house) # make all houses
        house.shop()
    
    # data for outputs
    global FW
    FW = pd.DataFrame(columns=['FW type', 'kg', 'Day', 'House'])
    
def run():
    for day in range(days):
        for house in houses:
            if day % house.shopping_frequency == 0:
                house.shop()
            house.eat()
            for food in house.menu:
                food.decay()

def FW_collect(house: House):
    for waste in house.waste_bin:
        FW._append({'FW type': waste.type, 'kg': waste.amount_kg, 'Day': waste.day_wasted, 'House': house.id},ignore_index=True)

def collect_data():
    for house in houses:
        FW_collect(house)     

def csv_out():
    FW.to_csv('FW_data', index=False)

def plot_weekly_food_waste(df):
    # cleaning
    day_sums = df.groupby(['Day', 'FW type'])['kg'].sum()
    totals = df.groupby('Day')['kg'].sum()
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plotting weekly totals by type
    plt.plot(totals['Day'], totals['kg'], label='Total')
    for FW_type in day_sums['FW type'].unique():
        cat = day_sums[day_sums['FW type'] == FW_type]
        plt.plot(cat['Day'], cat['kg'], label= FW_type)
    
    # Formatting the plot
    plt.xlabel('Day')
    plt.ylabel('kg')
    plt.title('FW')
    plt.legend()
    plt.grid(True)
    
    # Displaying the plot
    plt.show()

setup()
run()
collect_data()
csv_out()
