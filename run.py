from classes import House, Food, CookedFood, Store, Waste
def init(num_of_houses=100):
    store = Store()
    global houses
    for i in range(num_of_houses):
        house = House(id=i, store= store)
        houses.append(house)
        house.shop()

def run(days=54):
    for day in range(days):
        for house in houses:
            if day % house.shopping_frequency == 0:
                house.shop()
            