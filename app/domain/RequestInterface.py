from abc import ABC, abstractmethod

class RequestInterface(ABC):
    @abstractmethod
    def __init__(self, city):
        self.city = city

    @abstractmethod
    def get_cities_url_response(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_current_temp_response(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_week_temp_avg_response(self) -> str:
        raise NotImplementedError       
