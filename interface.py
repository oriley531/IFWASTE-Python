import run as r 
import output as op 

'''
Initilization 
Defaults:
    num_of_houses= 100:<int>
'''
r.init(num_of_houses=2)

'''
The function to run the simulation
Defaults:
    days = 365:<int>
'''
r.run(days=54)

'''
Output the data
Defaults: 
    line_graph=False 
    csv=True 
    excel=False
'''
op.create_outputs()