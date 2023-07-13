from IFWASTE_classes import House, Food, Waste, Store
import IFWASTE_output as output

#Initial Parameters
def setup():
    global days 
    days = 100 
    store = Store()
    global houses 
    houses = [] # stores houses
    num_of_houses = 2
    for i in range(num_of_houses):
        house = House(id = i, store= store)
        houses.append(house) # make all houses
        house.shop()

    # globals for outputs
    global FW_generation # Tracks the weekly generation rates of FW of all households combined.
    FW_generation = {"Total": [], "Dairy & Eggs": [], "Meat & Fish": [], "Fruits & Vegetables": [], "Dry Foods & Baked Goods": [], "Snacks, Condiments, Liquids, Oils, Grease, & Other": [], 'Cooked, Prepared Items, & Leftovers': []}

    global csv 
    csv = True
    global line_graph
    line_graph = True

    

def run():
    for day in range(days):
        for house in houses:
            if day % house.shopping_frequency == 0:
                house.shop()
            house.eat()
            for food in house.menu:
                food.decay()
        if day % 7 == 0 : # every 7 days
            FW_collect(houses, FW_generation) # collects and records the trash


def create_outputs():
    if line_graph == True:
        output.create_multi_plot_line_graph(FW_generation)
    if csv == True:
        output.write_dict_to_csv(FW_generation, 'FW_data')

def FW_collect(houses_to_collect: list, collect_to: dict):
    # Simulates the practice of a garbage truck coming to pick up all of the trash    
    week_FW = {"Total":0}
    for house in houses_to_collect:
        for FW in house.waste_bin:
            if FW.type in week_FW:
                week_FW[FW.type] += FW.amount_kg
            else:
                week_FW[FW.type] = FW.amount_kg
            week_FW["Total"] += FW.amount_kg
            house.waste_bin.remove(FW)
            del FW
    for FW in week_FW: # adds total week amount to the data list
        FW_generation[FW].append(week_FW[FW])


setup()
run()
create_outputs()
