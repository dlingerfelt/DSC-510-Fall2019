# File :    WeatherReport.py
# Name :    Pradeep Jaladi
# Date :    02/22/2020
# Course :  DSC-510 - Introduction to Programming
# Desc : Weather Report class which fetch the weather details from openweathermap.org.


import requests
import json
from JALADI_DSC510.final.Weather import Weather
from JALADI_DSC510.final.WeatherDisplay import WeatherDisplay
from requests.exceptions import HTTPError


class WeatherReport:
    # The app key of openweathermap.org, please change the key here if it changes.
    __appkey = '423a6cb4774d421801ce94e678be792b'

    # The open weather map url
    __initial_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + __appkey

    def __init__(self, weather: Weather):
        """ class initialize method, initializes url and weather model object """
        self.url = self.__initial_url
        self.weather = weather

    def fetch_weather(self) -> WeatherDisplay:
        """ Fetchs the weather for the zipcode or city specified """
        weather = self.weather
        try:
            # If zipcode is specified, construct the zipcode related url otherwise city url
            if weather.zipcode is None:
                self.url = self.url + '&q=' + weather.city
            else:
                self.url = self.url + '&zip=' + weather.zipcode

            # call the openweathermap.org url to get the weather details
            response = requests.get(self.url, timeout=10)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()

            # Processing the data returned by weather
            return self.process_data(response)

        except requests.ConnectionError as connectionError:
            print(f'OOPS!! Connection Error. Make sure you are connected to Internet : {connectionError}')
        except requests.Timeout as timeoutError:
            print(f'OOPS!! Timeout Error : {timeoutError}')
        except requests.RequestException as requestException:
            print(f'Invalid zipcode/city provided : {requestException}')
        except HTTPError as http_err:
            print(f'HTTP error occurred : {http_err}')
        except Exception as err:
            print(f'Other error occurred : {err}')

    def process_data(self, response) -> WeatherDisplay:

        # Converting the weather response to dictionary
        dict = json.loads(response.content)

        # Setting the values from dictionary to model
        city = dict['name']
        desc = dict['weather'][0]['description']
        country = dict['sys']['country']
        temp = dict['main']['temp']
        feels_like = dict['main']['feels_like']
        min_temp = dict['main']['temp_min']
        max_temp = dict['main']['temp_max']
        lat = dict['coord']['lat']
        lon = dict['coord']['lon']
        wind = dict['wind']['speed']

        # returning the weather display object
        return WeatherDisplay(desc, city, country, temp, feels_like, min_temp, max_temp, lat, lon, wind)
