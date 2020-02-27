# File :    Weather.py
# Name :    Pradeep Jaladi
# Date :    02/22/2020
# Course :  DSC-510 - Introduction to Programming
# Desc : Weather class which contains the properties of zipcode & city.

class Weather:

    def __init__(self):
        """ class initialize method,  initializes zipcode & city to None """
        self._zipcode = None
        self._city = None

    @property
    def zipcode(self):
        """ Returns zip code """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """ Sets the property zip code """
        self._zipcode = zipcode

    @property
    def city(self):
        """ Returns city """
        return self._city

    @city.setter
    def city(self, city):
        """ Sets the property city """
        self._city = city
