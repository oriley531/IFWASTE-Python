import IFWASTE_classes
import IFWASTE_graphing

def setup():
    num_of_houses = 100
    FW_generation = []
    houses = []
    days_to_run = 100
    for i in range(num_of_houses) :
        house = House()
        houses.append(house)
        house.shop()

def run(days) :
    for day in range(days):
        for house in houses:
            if day % 3 == 0:
                house.shop # shops every 3 days
            for i in 3 :
                house.eat() # eat 3 meals a day
            for food in house.menu:
                food.decay() # food decays
        if day % 7 == 0 :
            FW_collect()
    create_multi_plot_line_graph(FW_generation)
    write_dict_to_csv(FW_generation, 'outputdata')

setup()
run(days_to_run)