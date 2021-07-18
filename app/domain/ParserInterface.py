from abc import ABC, abstractmethod

class ParserInterface(ABC):
    @abstractmethod
    def parse_city_url_data(self, data):
        raise NotImplementedError
    
    @abstractmethod
    def parse_current_temp_data(self, data):
        raise NotImplementedError

    @abstractmethod
    def parse_min_temp_data(self, data):
        raise NotImplementedError

    @abstractmethod
    def parse_max_temp_data(self, data):
        raise NotImplementedError      