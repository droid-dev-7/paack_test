import sys, os
from requests.api import request
import getopt

sys.path.append(os.path.abspath(".."))
from app.actions.WeatherActions import WeatherActions
from app.adapter.RequestAdapter import RequestAdapter
from app.adapter.XmlParser import XmlParser

class ElTiempo():
    def help(self):
        usage = ('''Usage:
            eltiempo.py -today 'Gavá'
            eltiempo.py -av_max 'Gavá'
            eltiempo.py -av_min 'Gavá'
            ''')
        raise SystemExit(usage)

    def parse(self):
        if((len(sys.argv) - 1) != 2):
            self.help()

        full_cmd_arguments = sys.argv
        argument_list = full_cmd_arguments[1:]
        short_options = 't:h:l:'
        long_options = ["today=", "av_max=","av_min="]
        try:
            arguments, values = getopt.getopt(argument_list, short_options, long_options)
        except getopt.error as err:
            raise SystemExit(err)

        return arguments

    def run(self):
        arguments = self.parse()
        for current_argument, city in arguments:
            if  "--today" in current_argument:
                request_adapter = RequestAdapter(city)
                parser = XmlParser()
                weather_actions = WeatherActions(city, request_adapter, parser)
                current_temp = weather_actions.get_current_temp()
                message = "The current temperature in " +  city + " is " + current_temp
                print (message)
                return message
            elif "--av_max" in current_argument:
                request_adapter = RequestAdapter(city)
                parser = XmlParser()
                weather_actions = WeatherActions(city, request_adapter, parser)
                min_temp = weather_actions.get_max_avg_temp()
                message = "The weekly average max temperature in " +  city + " is " + min_temp
                print (message)
                return message
            elif "--av_min" in current_argument:
                request_adapter = RequestAdapter(city)
                parser = XmlParser()
                weather_actions = WeatherActions(city, request_adapter, parser)
                max_temp = weather_actions.get_min_avg_temp()
                message = "The weekly average min temperature in " +  city + " is " + max_temp
                print (message)
                return message
            else:
                self.help()

    def main(self, argv):
        return self.run()
        
if __name__ == "__main__":
    ElTiempo().main(sys.argv[1:])