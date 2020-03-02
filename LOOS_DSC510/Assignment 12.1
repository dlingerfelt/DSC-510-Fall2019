#Weather Forecast Generator
#File: Assignment 12.1
#Name: Michael Loos
#Date: 2/24/2020

import requests
import json
from datetime import datetime

#function to check if entry is zip code or city
def input_check(entry):
  #remove spaces from city name
  entry=entry.replace(" ","")

  #assign and return querystring based on alpha or numeric
  if entry.isdigit()==True:
    querystring=zip_code(entry)
  elif entry.isalpha()==True:
    querystring=city(entry)
  else:
    print('Entry Error. Input should be a zip code or city.\n')
    return False
  return querystring

#define query string if entry is zip
def zip_code(entry):
  querystring={"zip":entry,"units":"imperial", "APPID":"bbe79b471c70a334b0f73ed365290378"}
  return querystring

#define query string if entry is city
def city(entry):
  querystring={"q":entry,"units":"imperial", "APPID":"bbe79b471c70a334b0f73ed365290378"}
  return querystring

#function for current conditions
def current_cond(querystring):
  #url, headers, and querystring
  url="http://api.openweathermap.org/data/2.5/weather?"
  headers={'cache-control':'no-cache'}

  #try block for connection response
  try:
    response=requests.request("GET",url,headers=headers,params=querystring)
    response.raise_for_status()
  except requests.exceptions.RequestException:
    print('Connection Error: {}\nMake sure input is valid zip code or city.\n'.format(response))
    return False
  if 200<=response.status_code<=299:
    print('Connection Successful!')

  #get JSON data
  dic=(response.text)
  info = json.loads(dic)

  #print current conditions from JSON data
  print("\nCurrent conditions for {}".format(info['name']))
  new_list=info['weather']

  #iterate through JSON list for dictionary
  for new_dic in new_list:
    print('Sky: {}'.format(new_dic['main']))

  #new dictionary from info entry
  new_dic2=info['main']

  #print current Temperature, Wind Chill, and Humidity from new_dic2
  print('Temperature: {}\N{DEGREE SIGN}F'.format(round(new_dic2['temp'])))
  print('Feels Like: {}\N{DEGREE SIGN}F'.format(round(new_dic2['feels_like'])))
  print('Humidy: {}%'.format(new_dic2['humidity']))

  return

def forecast(querystring):
  url="http://api.openweathermap.org/data/2.5/forecast?"
  headers={'cache-control':'no-cache'}

  #try block for connection response
  try:
    response=requests.request("GET",url,headers=headers,params=querystring)
    response.raise_for_status()
  except requests.exceptions.RequestException:
    print('Forecast Connection Error: {}\nMake sure input is valid zip code or city.\n'.format(response))
    return False
  if 200<=response.status_code<=299:
    print('\nForecast Connection Successful!')

  #get JSON data
  dic=(response.text)
  info = json.loads(dic)

  print('\nForecast: ')

  #iterate through JSON data for each forecast entry
  for item in info['list']:
    #get datetime, temperature, and sky conditions
    temperature=round(item['main']['temp'])
    sky=item['weather'][0]['main']

    #format date and time
    date_string = item['dt_txt']
    time=(datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I %p'))

    #print date, time, temperature, and sky condition
    print('{}: {}\N{DEGREE SIGN}F and {}'.format(time,temperature,sky))
  return

#main function
def main():
  #welcome message
  print('Welcome to the weather machine. Enter Quit to exit.')

  #loop for zip or city until user quits
  while True:
    entry=input("\n\nEnter zip code or city: ")
    if entry.lower()!='quit':
      querystring=input_check(entry)

      #go back through loop if invalid entry
      if querystring==False:
        continue
      #call current conditions and forecast functions
      current_cond(querystring)
      forecast(querystring)
    else:
      print('Exiting...')
      break
  return

main()
