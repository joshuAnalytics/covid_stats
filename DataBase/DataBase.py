from abc import ABC, abstractmethod

class DataBase(ABC):
    def __init__(self, data_dir: str):
        self.data_dir: str = data_dir
        
    @abstractmethod
    def pull_data(self):
        pass

    @abstractmethod
    def update_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass

