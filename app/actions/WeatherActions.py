from app.domain.ParserInterface import ParserInterface
from app.domain.RequestInterface import RequestInterface
import sys

class WeatherActions(): 
    def __init__(self, city, request_adapter: RequestInterface, parser : ParserInterface):
        self.city = city
        self.request_adapter = request_adapter
        self.parser = parser

    def get_city_url(self):
        response = self.request_adapter.get_cities_url_response()
        try:
            city_url = self.parser.parse_city_url_data(response.text, self.city)
        except ValueError as err:
            raise SystemExit(err)
        return city_url

    def get_current_temp(self):
        city_url = self.get_city_url()
        response = self.request_adapter.get_current_temp_response(city_url)
        try:
            current_temp = self.parser.parse_current_temp_data(response.text)
        except ValueError as err:
            raise SystemExit(err)
        return current_temp

    def get_max_avg_temp(self):
        city_url = self.get_city_url()
        response = self.request_adapter.get_week_temp_avg_response(city_url)
        try:
            max_avg_temp = self.parser.parse_max_temp_data(response.text)
        except ValueError as err:
            raise SystemExit(err)         
        return max_avg_temp

    def get_min_avg_temp(self):
        city_url = self.get_city_url()
        response = self.request_adapter.get_week_temp_avg_response(city_url)
        try:
            min_avg_temp = self.parser.parse_min_temp_data(response.text)
        except ValueError as err:
            raise SystemExit(err)  
        return min_avg_temp
