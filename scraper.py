import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def scrape_website():
    data = requests.get("https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data")
    soup = BeautifulSoup(data.text, "html.parser")
    return soup

def get_countries(soup):
    countries = {}
    i = 0
    for th in soup.find_all("th", { "scope": "row"}):
        for a in th.find_all("a"):
            if "title" in a.attrs:
                countries[i] = a.text
                i+=1
    return countries

def get_numbers(soup):
    numbers = {}
    i = 0
    for td in soup.find_all("td"):
        numbers[i] = td.text.replace('\n', '')
        i+=1
    return numbers

def generate_dataframe(countries,numbers):
    numbers_df = pd.Series(numbers)
    countries_df = pd.Series(countries)
    
    #get the cases,deaths and recovered numbers for each country
    num_rows = len(countries_df) * 4
    first_row = 0
    last_row = 4
    data = []
    
    for country in countries_df:
        row_numbers = numbers_df.iloc[first_row:last_row].values
        cases = row_numbers[0].replace(",","")
        deaths = row_numbers[1].replace(",","")
        recov = row_numbers[2].replace(",","")
        row = {"country":country,
            "cases": cases,
            "deaths": deaths,
            "recov": recov
            }
        data.append(row)
        first_row +=4
        last_row +=4
    
    df = pd.DataFrame(data)
    #remove non alpha chars
    df.replace("-",value=np.nan,inplace=True)
    df.replace("–",value=np.nan,inplace=True)
    df.replace("—",value=np.nan,inplace=True)
    df.replace(" ",value=np.nan,inplace=True)
    
    #remove the rows with text
    df = df.loc[~df['cases'].str.contains("[A-Za-z]")]
    
    #check if dataframe contains any strings
    assert df['cases'].str.contains("[A-Za-z]").any() == False
    
    #set empty fields as null
    df.replace("",np.NaN,inplace=True)
    
    #convert to float
    df.loc[:,'cases'] = df['cases'].astype(float).copy()
    df.loc[:,'deaths'] = df['deaths'].astype(float).copy()
    df.loc[:,'recov'] = df['recov'].astype(float).copy()
    
    df = df.set_index('country')
    return df

def get_latest_data():
    soup = scrape_website()
    countries = get_countries(soup)
    numbers = get_numbers(soup)
    df = generate_dataframe(countries,numbers)
    print(df.head())
    return df

if __name__ == "__main__":
    get_latest_data()