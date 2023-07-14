import run as r
import numpy as np 
import pandas as pd

def FW_collect(shopping_data=False, waste_data=True):
    if waste_data == True:
        global FW
        FW = pd.DataFrame(columns=['House id', 'Day Wasted', 'kg', 'Type'])
        #collect the data for data analysis and interpretation
        for house in r.houses:
            for item in house.waste_bin:
                new_W = {
                    'House id': house.id, 
                    'Day Wasted': item.day_wasted, 
                    'kg': item.amount_kg, 
                    'Type': item.type
                }
                FW.loc[len(FW)] = new_W
    if shopping_data == False:
        print('Collecting Shopping Data is not yet implemented')

def create_outputs(line_graph=False, csv=True, excel=False):
    if line_graph == True:
        create_linegraph()
    if csv == True:
        FW.to_csv('FW_data.csv')
    if excel == True:
        FW.to_excel('FW_data.xlsx')