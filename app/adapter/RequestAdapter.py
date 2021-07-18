from app.domain.RequestInterface import RequestInterface

import requests
from requests.exceptions import HTTPError

affiliate_id = '&affiliate_id=rf4pjeh31f3p'
bcn_cities_url = 'http://api.tiempo.com/index.php?api_lang=es&division=102' + affiliate_id
hourly_attr = '&v=2.0&h=1'
timeout = 5

class RequestAdapter(RequestInterface): 
    def __init__(self, city):
        super().__init__(city)

    def get_response(self, url):
        try:
            response = requests.get(url, timeout)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            raise SystemExit(errh)
        except requests.exceptions.ConnectionError as errc:
            raise SystemExit(errc)
        except requests.exceptions.Timeout as errt:
            raise SystemExit(errt)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        return response

    def get_cities_url_response(self) -> str:
        response = ""
        response = self.get_response(bcn_cities_url)
        return response

    def get_current_temp_response(self, city_url) -> str:
        response = ""
        response = self.get_response(city_url + affiliate_id + hourly_attr)
        return response

    def get_week_temp_avg_response(self, city_url) -> str:
        response = ""
        response = self.get_response(city_url + affiliate_id)
        return response
