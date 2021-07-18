from app.domain.ParserInterface import ParserInterface
import xml.etree.ElementTree as ET
from app.domain.Time import Time

class XmlParser(ParserInterface):
    def parse_city_url_data(self, data, city_name):
        url = None
        tree = ET.ElementTree(ET.fromstring(data))
        root = tree.getroot()
        for location in root.findall('location'):
            for city in location.findall('data'):
                name = city.find('name').text
                if(name in city_name):
                    url = city.find('url').text
                    return url
        if(url is None):
            raise ValueError("The temperature for the requested city is not available")
        return url
    
    def parse_current_temp_data(self, data):
        temp = None
        tree = ET.ElementTree(ET.fromstring(data))
        root = tree.getroot()
        time = Time()
        current_hour = time.get_current_time()
        for location in root.findall('location'):
            for day in location.findall('day'):
                for hour in day.findall('hour'):
                    if(current_hour in hour.get('value')):
                        for temp_aux in hour.findall('temp'):
                            temp = temp_aux.get('value')
                            return temp
        if(temp is None):
            raise ValueError("The current temperature for the requested city is not available")                      
        return temp

    def parse_avg_temp_data(self, max: bool, data):
        tree = ET.ElementTree(ET.fromstring(data))
        root = tree.getroot()
        days = 0
        avg_temp = None
        agg_temp_aux = 0
        min_max_temp_str = "Máx" if max else "Mín"
        for location in root.findall('location'):
            for var in location.findall('var'):
                if days >= 7:
                    avg_temp = str(round(agg_temp_aux / days, 2))
                    return avg_temp
                for data in var.findall('data'):
                        for forecast in data.findall('forecast'):
                            name = var.find('name').text
                            if(name.find(min_max_temp_str) != -1):
                                temp = int(forecast.get('value'))
                                agg_temp_aux = agg_temp_aux + temp 
                                days = days + 1 
        if(avg_temp is None):
            raise ValueError("The average temperature for the requested city is not available")    
        return avg_temp 

    def parse_min_temp_data(self, data):
        return self.parse_avg_temp_data(False, data)

    def parse_max_temp_data(self, data):
        return self.parse_avg_temp_data(True, data)  
