# File :    WeatherDisplay.py
# Name :    Pradeep Jaladi
# Date :    02/22/2020
# Course :  DSC-510 - Introduction to Programming
# Desc : Weather Display class displays the weather details to output.

class WeatherDisplay:

  def __init__(self, desc, city, country, temp, feels_like, min_temp, max_temp, lat, lon, wind):
    """ Initialize the model variables """
    self._desc = desc
    self._city = city
    self._country = country
    self._temp = temp
    self._feels_like = feels_like
    self._min_temp = min_temp
    self._max_temp = max_temp
    self._lat = lat
    self._lon = lon
    self._wind = wind

  def print_report(self):
    """ Prints the details to the output screen """
    print('---------------------------------------------------------------------------------------')

    print('Current temperature is : %df' % self.__convert_temp(self._temp))
    print('outside it looks like  : {}'.format(self._desc))
    print('Current it feels like  : %df' % self.__convert_temp(self._feels_like))
    print('Wind outside is        : %d miles per hour' % self.__convert_wind(self._wind))
    print('City                   : {}, {}'.format(self._city, self._country))
    print('coordinates are        : [{}, {}]'.format(self._lat, self._lon))
    print('Today the temperatures are High as %df and low as %df' % (
    self.__convert_temp(self._max_temp), self.__convert_temp(self._min_temp)))

    print('---------------------------------------------------------------------------------------')

  def __convert_temp(self, kelvin: float) -> float:
    """ converts the temperature from kelvin to f """
    return 9 / 5 * (kelvin - 273.15) + 32

  def __convert_wind(self, meter: float) -> float:
    """ converts the wind from meter to miles per hour """
    return meter * 2.2369363
