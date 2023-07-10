from IFWASTE_classes import House, Food, Waste
import IFWASTE_graphing as output

#Initial Parameters
num_of_houses = 2
houses = []
days = 100
for i in range(num_of_houses) :
    house = House()
    house.shop()
    houses.append(house)

#Run
for day in range(days):
    for house in houses:
        if day % 1 == 0:
            house.shop() # shops every 3 days
        for i in range(3) :
            house.eat() # eat 3 meals a day
        for food in house.menu:
            food.decay() # food decays
    if day % 7 == 0 :
        output.FW_collect(houses)


# Output
output.create_multi_plot_line_graph(output.FW_generation)
output.write_dict_to_csv(output.FW_generation, 'outputdata')
