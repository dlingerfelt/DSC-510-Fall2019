'''
 File: DSC510-Week 12 Nguyen.py
 Name: Chau Nguyen
 Date: 3/1/2020
 Course: DSC_510 Intro to Programming
 Description: Finale Project: creating a weather program to get today's weather using requests library and API key.
 '''
import json
import requests
import datetime #import date module
def API_requests(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #Combined inputed city, API key and base url for .get()
    complete_url = base_url + "appid=b5549742bd446884c3ae3e008f5fa7ed" + "&q=" + city + "&units=imperial"
    # Try and Except block for URL error
    try:
        response = requests.get(complete_url)
        x = response.json() #load json data
        if x["cod"] == "404":
            raise Exception
    except Exception as e:
        print('Invalid Input! Please double check City name or Zipcode')
    return x
# prettyprint function to nice display result
def prettyprint(weather_data):
    city_name = weather_data["name"]
    location = weather_data["sys"]
    country = location['country']
    #country = location[0]["country"]
    temp = weather_data["main"]
    current_temperature = temp["temp"]
    feels_like = temp["feels_like"]
    temp_max = temp["temp_max"]
    temp_min = temp["temp_min"]
    humidity = temp["humidity"]
    weather_desciption = weather_data["weather"]
    description = weather_desciption[0]["description"]
    dayz = datetime.datetime.now()
    print('Today {}, {},'.format(dayz.strftime("%A"),dayz.strftime("%m/%d/%Y")))
    print('Current weather in {},{} is'.format(city_name,country))
    print(" It's showing  " +
                    str(description) +
          "\n Temperature " +
                    str(current_temperature) + " F" +
          "\n feels like " +
                    str(feels_like) +
          "\n Highest Temperature today " +
                    str(temp_max) +
          "\n Lowest Temperature is " +
                    str(temp_min) +
          "\n Humidity is "+
                    str(humidity))
def main():
    print("This program is design to help check today's weather.")
    user_input = ''
    program = True
    while True:
        try:
            user_input = input("Enter city name or zipcode to check weather, else enter 'exit' ")
            if user_input.lower() == 'exit':
                program = False
                break
            else:
                city = user_input #rename user_input to city
                weather_data = API_requests(city)
            prettyprint(weather_data)
        except:
            print('Please enter again')
    print("End program")
if __name__ == '__main__':
    main()


