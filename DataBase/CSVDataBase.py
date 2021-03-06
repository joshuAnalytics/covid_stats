import json
import scraper
import urllib
import requests
import pandas as pd
import streamlit as st
from pathlib import Path
from datetime import date
from DataBase.DataBase import ABCDataBase


class CSVDataBase(ABCDataBase):
    '''
    Data is stored in and loaded from CSVs.
    '''
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def pull_data(self):
        '''Pulls from all data sources and stores in CSV files'''
        pass

    def update_data(self):
        '''Pulls data from sources that change daily and stores in CSV files'''
        pass

    def load_data(self):
        '''Loads data from CSV files'''
        pass

    def _get_csv_from_url(self, url, outfile):
        """
        download a csv from a url
        """
        filename = url[url.rfind("/") + 1:]
        filepath = '_data/' + outfile
        urllib.request.urlretrieve(url, filepath)
        return

    def _get_world_bank_data(self, file_path, data_name):
        # http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv
        df = pd.read_csv(file_path, skiprows=4)
        series = df.set_index('Country Name')['2018']
        series.name = data_name

        # fix the mismatched names in the world bank data
        with open('name_mapping.json') as json_file:
            name_mapping = json.load(json_file)

        data = series.reset_index()
        data['Country Name'].replace(name_mapping, inplace=True)
        data.set_index('Country Name', inplace=True)

        return data

    def _join_world_bank_data(self):
        # get pop density
        # http://api.worldbank.org/v2/en/indicator/EN.POP.DNST?downloadformat=csv
        pop_density = self._get_world_bank_data(
            'API_EN.POP.DNST_DS2_en_csv_v2_936296.csv',
            'pop_density'
            )

        # get population
        # http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv
        pop_total = self._get_world_bank_data(
            'API_SP.POP.TOTL_DS2_en_csv_v2_936048.csv',
            'pop_total'
            )

        wb_data = pd.concat([pop_density, pop_total], axis=1)
        return wb_data

    def _join_data_sources(self):
        df = scraper.get_latest_data()
        df = df.join(self._join_world_bank_data())
        return df

    def _generate_features(self, df):
        df['deaths_per_million'] = df['deaths'] / df['pop_total'] * 1000000
        df['cases_per_million'] = df['cases'] / df['pop_total'] * 1000000

        # calculate additional metrics
        df['death_rate_%'] = df['deaths'] / df['cases'] * 100
        return df

    def _get_latest_apple_url(self):
        host = "https://covid19-static.cdn-apple.com"
        json_path = "/covid19-mobility-data/current/v2/index.json"
        response = requests.get(host + json_path)
        response_json = json.loads(response.text)
        csv_path = response_json['regions']['en-us']['csvPath']
        base_path = response_json['basePath']
        full_url = host + base_path + csv_path
        return full_url

    def import_static_data(self):
        df = self._join_data_sources()
        df = self._generate_features(df)
        return df

    def get_csse_time_series_deaths(self):
        df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
        meta_cols = ['Province/State', 'Country/Region', 'Lat', 'Long']
        time_series = df.drop(meta_cols, axis=1)

        # get a unique country name to use as id
        df['Province/State'] = df['Province/State'].fillna("")
        df['country'] = df['Country/Region'] + " " + df['Province/State']
        df['country'] = df['country'].str.rstrip()

        # pivot the dataframe
        time_series = time_series.T
        time_series.columns = df['country']

        # melt countries and deaths into single column
        df_melted = pd.melt(time_series.reset_index(), id_vars=["index"])
        df_melted.columns = ['date', 'country', 'deaths']
        df_melted['date'] = pd.to_datetime(df_melted['date'])

        return df_melted

    @st.cache()
    def get_apple_movement_indices(self, movement_type='walking'):
        """
        get latest time series data from apple on population movement by country
            - movement_type <str> enum "walking"|"driving|"transit"
        """

        try:
            url = self._get_latest_apple_url()
            df = pd.read_csv(url)

        except:
            df = pd.read_csv("_data/applemobilitytrends-latest.csv")

        meta_cols = ['geo_type', 'region', 'transportation_type']

        # filter by movement type
        df_walk = df.loc[df['transportation_type'] == movement_type]
        assert df_walk['region'].is_unique
        time_series = df_walk.drop(meta_cols, axis=1)

        # pivot the dataframe
        time_series = time_series.T
        time_series.columns = df_walk['region']

        # melt countries and y vals into single column
        df_melted = pd.melt(time_series.iloc[:, :].reset_index(), id_vars=['index'])
        df_melted.columns = ['date', 'country', 'movement_index']
        df_melted['date'] = pd.to_datetime(df_melted['date'], errors='coerce')
        return df_melted

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--update', '-U', help='updates daily data sources')
    # parser.add_argument('--all', '-A', help='updates all data sources')
    # args = parser.parse_args()

    data_dir = Path.cwd() / 'data'
    CSVDataBase(data_dir).update_data()
