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
Create the desired outputs
Defaults:
    line_graph = True 
    csv = False

'''
op.create_outputs(FW_generation= r.FW_generation)