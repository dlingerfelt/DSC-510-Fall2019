from flask import Flask, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)


class WeatherReport(Resource):

    def get(self, zip_code):
        open_weather_url = "https://api.openweathermap.org/data/2.5/weather"
        # This function connects to the chuck norris API and executes its get method.
        # The response is converted to JSON and the joke is obtained from the key 'value'.
        # This function is called by main.
        try:
            querystring = {"zip": zip_code, "APPID": "f985b93ed77c52ad1dc90147bb8aa29e"}
            headers = {'cache-control': 'no-cache'}
            response = requests.get(open_weather_url, headers=headers, params=querystring)
            if response.status_code != 200:
                print('Error requesting Get ' + str(response.status_code))
                exit(response.status_code)
            else:
                print('Success in getting web service ' + str(response.status_code))
            temp_pressure_humidity = response.json()['main']
            return self.kelvin_to_fahrenheit(temp_pressure_humidity['temp'])
        except:
            exit('Exception connecting to open_weather_url API!!')

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return ((float(kelvin) - 273.15) * 1.8) + 32


api.add_resource(WeatherReport, '/<zip_code>')
if __name__ == '__main__':
    app.run(port='5009')
