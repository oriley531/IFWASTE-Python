import run as r
import numpy as np 
import pandas as pd

def create_outputs(line_graph=False, csv=True, excel=False):
    if line_graph == True:
        create_linegraph()
    if csv == True:
        r.FW.to_csv('FW_data.csv', index=False)
    if excel == True:
        r.FW.to_excel('FW_data.xlsx')

