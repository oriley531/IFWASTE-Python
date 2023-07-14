from classes import House, Food, Waste, Store
import output as output

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
            house.day = day
            if day % house.shopping_frequency == 0:
                house.shop()
            house.eat()
            for food in house.menu:
                food.decay()
