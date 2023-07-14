import run as r 
from classes import House, Food, Waste, Store
import output as op 

'''
Initilization 
Defaults:
    num_of_houses= 100:<int>
'''
r.init()

'''
The function to run the simulation
Defaults:
    days = 365:<int>
'''
r.run()

''' 
Collect the data you want
Defaults:
    shopping_data=False 
    waste_data=True
'''
op.FW_collect()

'''
Output the data
Defaults: 
    line_graph=False 
    csv=True 
    excel=False
'''
op.create_outputs()