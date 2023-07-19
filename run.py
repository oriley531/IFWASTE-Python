from classes import House, Food, Waste, Store
import numpy as np 
import pandas as pd
#Initial Parameters
def init(num_of_houses=100):
    store = Store()
    global houses 
    houses = [] # stores houses
    for i in range(num_of_houses):
        house = House(id = i, store= store)
        houses.append(house) # make all houses
        house.shop()

def run(days=365):
    for day in range(days):
        for house in houses:
            if day % house.shopping_frequency == 0:
                house.shop()
                house.check_pantry()
            house.eat()
            FW_collect(day=day, house= house)
            for food in house.menu:
                food.decay()
            
def FW_collect(day, house:House):
    if day == 0:
        global FW
        FW = pd.DataFrame(columns=['House id', 'Day Wasted', 'kg', 'Type'])
    #collect the data for data analysis and interpretation
    for item in house.waste_bin:
        new_W = {
            'House id': house.id, 
            'Day Wasted': day, 
            'kg': item.amount_kg, 
            'Type': item.type
        }
        house.waste_bin.remove(item)
        del item
        FW.loc[len(FW)] = new_W