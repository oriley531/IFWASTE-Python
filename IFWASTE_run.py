from IFWASTE_classes import House, Food, Waste
import IFWASTE_output as output

#Initial Parameters
def setup():
    # Initialize and define the global variables that will be used throughout the run.
    global FW_generation # Tracks the weekly generation rates of FW of all households combined.
    FW_generation = {"Total": [], "Meat & Fish": [], "Dairy & Eggs": [], "Fruits and Vegetables": [], "Baked Goods": [], "Dry Foods": [], "Snacks, Condiments, & Other": [], "Cooked/Prepared Items/Leftovers": [], "Liquids/Oils/Grease": []}
    global days # the number of days you would like to run for
    days = 100 
    global houses # a list that contains all of the houses simulated
    houses = []
    num_of_houses = 2 # the amount of houses simulated
    # Create all of the houses and add them to the list
    for i in range(num_of_houses) :
        house = House()
        house.shop()
        houses.append(house)
    # Output Options 
    # Make True to recieve them
    global csv 
    csv = False
    global line_graph
    line_graph = True
    

def run():
    for day in range(days): # runs the test period
        for house in houses:
            if day % house.shopping_frequency == 0:
                house.shop() # shopping every x days
            for i in range(3) :
                house.eat() # eat 3 meals a day
            for food in house.menu:
                food.decay() # food decays
        if day % 7 == 0 : # every 7 days
            FW_collect(houses, FW_generation) # collects and records the trash


def create_outputs():
    if line_graph == True:
        output.create_multi_plot_line_graph(FW_generation)
    if csv == True:
        output.write_dict_to_csv(FW_generation, 'outputdata')

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
