"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: December 5th 2019
Program Description: Holds information about a single country.
"""


# the class Country, a Country object consists of the country's name, continent, population and area
class Country:

    # the constructor, sets instance variables to specified values
    def __init__(self, name, cont, pop, area):
        self._name = name
        self._cont = cont
        self._pop = pop
        self._area = area

    # returns the name of the country
    def getName(self):
        return self._name

    # returns the population of the country
    def getPopulation(self):
        return self._pop

    # returns the area of the country
    def getArea(self):
        return self._area

    # returns the continent of the country
    def getContinent(self):
        return self._cont

    # sets the population of the country to a specified value
    def setPopulation(self, pop):
        self._pop = pop

    # sets the area of the country to a specified value
    def setArea(self, area):
        self._area = area

    # sets the continent of the country to a specified value
    def setContinent(self, cont):
        self._cont = cont

    # creates a string representation of the country object
    def __repr__(self):
        return self._name + " (pop: " + self._pop + ", size: " + self._area + ") in " + self._cont
