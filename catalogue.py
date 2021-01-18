"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: December 5th 2019
Program Description: Holds information about a catalogue.
"""

# import statement
from country import *


# the class CountryCatalogue, an object of this class is a set of countries
class CountryCatalogue:

    # the constructor, opens the data file and creates a catalogue
    def __init__(self, countryFile):

        # initializes instance variable for the set of countries
        self._countryCat = set()

        # reads file, determines the name, continent, area and population of the countries and adds them to the set
        for line in countryFile:

            # checks to see if there's a header, removes if necessary
            if not line.startswith("Country"):

                # splits the line and makes a country based on amount of information and the data
                words = line.strip("\n").split("|")
                if len(words) == 1:
                    self._countryCat.add(Country(words[0], "", "", ""))
                if len(words) == 2:
                    self._countryCat.add(Country(words[0], words[1], "", ""))
                if len(words) == 3:
                    self._countryCat.add(Country(words[0], words[1], words[2], ""))
                if len(words) > 3:
                    self._countryCat.add(Country(words[0], words[1], words[2], words[3]))

    # sets the population of a country in the catalogue
    def setPopulationOfCountry(self, name, pop):

        # checks to make sure the country exists and there is an actual update
        if self.findCountryByName(name) is not None and pop != "":

            # sets the population
            self.findCountryByName(name).setPopulation(pop)

    # sets the area of a country in the catalogue
    def setAreaOfCountry(self, name, area):

        # checks to make sure the country exists and there is an actual update
        if self.findCountryByName(name) is not None and area != "":

            # sets the area
            self.findCountryByName(name).setArea(area)

    # sets the continent of a country in the catalogue
    def setContinentOfCountry(self, name, cont):

        # checks to make sure the country exists and there is an actual update
        if self.findCountryByName(name) is not None and cont != "":

            # sets the continent
            self.findCountryByName(name).setContinent(cont)

    # searches for a country in the catalogue, returns the country if it exists
    def findCountry(self, country):

        # for loop that searches for a country in the catalogue by country, returns the country if found
        for i in self._countryCat:
            if country.getName() == i.getName():
                return i

        # returns none if there is no country
        return None

    # searches for a country in the catalogue based on its name, returns the country object if it exists
    def findCountryByName(self, name):

        # for loop that searches for a country in the catalogue by name, returns the country if found
        for i in self._countryCat:
            if name == i.getName():
                return i

        # returns none if there is no country with that name
        return None

    # adds a country to the catalogue
    def addCountry(self, countryName, cont, pop, area):

        # for loop that checks for the country already existing in the catalogue, returns false if it does
        for country in self._countryCat:
            if country.getName() == countryName:
                return False

        # creates country bad on parameters if it does not exist
        self._countryCat.add(Country(countryName, cont, pop, area))

        # returns true if the country has been successfully added
        return True

    # prints each country of the catalogue
    def printCountryCatalogue(self):

        # for loop that goes through the catalogue and prints each country
        for country in self._countryCat:
            print(country)

    # outputs the catalogue into a file
    def saveCountryCatalogue(self, fname):

        # opens/creates the output file
        try:
            outf = open(fname, "w")
        except IOError:
            return -1

        # sorts the set of countries in the catalogue and puts them in a list
        listOfCountries = sorted(self._countryCat, key=lambda c: c.getName())

        # writes the information in the file
        outf.write("Country|Continent|Population|Area\n")
        for country in listOfCountries:
            outf.write(country.getName() + "|" + country.getContinent() + "|" + country.getPopulation() + "|" + country.getArea() + "\n")

        # returns the amount of countries in the catalogue
        return len(self._countryCat)


