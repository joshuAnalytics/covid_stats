import pandas as pd
import json

def get_pop_density():
    #http://api.worldbank.org/v2/en/indicator/EN.POP.DNST?downloadformat=csv
    df = pd.read_csv('API_EN.POP.DNST_DS2_en_csv_v2_936296.csv',skiprows=4)
    pop_density = df.set_index('Country Name')['2018']
    pop_density.name = "pop_density"
    
    #fix the mismatched names in the world bank data
    with open('name_mapping.json') as json_file:
        name_mapping = json.load(json_file)
    
    pop_density = pop_density.reset_index()
    pop_density['Country Name'].replace(name_mapping,inplace=True)
    pop_density.set_index('Country Name',inplace=True)
    
    return pop_density
