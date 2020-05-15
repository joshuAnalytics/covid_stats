from covid_stats import DataBase

class CSVDataBase(DataBase):
    '''
    Data is stored in and loaded from CSVs.  
    '''
    def __init__(self, data_dir: str):
        self.data_dir: str = data_dir

    def pull_data(self):
        '''Pulls from all data sources and stores in CSV files'''
        pass

    def update_data(self):
        '''Pulls data from sources that change daily and stores in CSV files'''
        pass

    def load_data(self):
        '''Loads data from CSV files'''
        pass