"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: December 5th 2019
Program Description: Updates a file with country data.
"""

# import statement
from catalogue import *


# function that applies updates to a file of countries with data, then outputs the updated information into a file
def processUpdates(cntryFileName, updateFileName):

    # while loop that keeps asking for input if it is incorrect
    while True:

        # tries to open the country data file
        try:
            cfile = open(cntryFileName, "r")
            break

        # if the file does not exist, prompts for file name again
        except IOError:

            # if the user wants to try again
            if input("Country file does not exist. Quit (Y) or try again (N). ").lower() == "n":
                cntryFileName = input("Enter country file name. ")

            # if the user does not want to try again
            else:

                # tries to open the output file, prints error message if it fails to open
                try:
                    outf = open("output", "w")
                except IOError:
                    print("Error with opening output file. ")
                    return False

                # writes to output file and returns false
                outf.write("Update Unsuccessful\n")
                return False

    # while loop that keeps asking for input if it is incorrect
    while True:

        # tries to open the country update file
        try:
            ufile = open(updateFileName, "r")
            break

        # if the file does not exist, prompts for file name again
        except IOError:

            # if the user wants to try again
            if input("Update file name does not exist. Quit (Y) or try again (N). ").lower() == "n":
                updateFileName = input("Enter update file name. ")

            # if the user does not want to try again
            else:

                # tries to open the output file, prints error message if it fails to open
                try:
                    outf = open("output", "w")
                except IOError:
                    print("Error with opening output file. ")

                # writes to output file and returns false
                outf.write("Update Unsuccessful\n")
                return False

    # creates country catalogue based on country data file
    catalogue = CountryCatalogue(cfile)

    # analyzes each line in the update file
    for line in ufile:

        # splits the words based on semicolons
        words = line.split(";")

        # checks to make sure the format is correct
        if len(words) > 1 and len(words) == line.count("=") + 1:

            # resets data variables
            pop = ""
            cont = ""
            area = ""

            # for loop that determines each update value
            for i in range(1, len(words)):

                # strips newline
                upd = words[i].strip("\n")

                # based on what the section starts with, splits it to get the value and sets the appropriate variable to it
                if upd.startswith("P="):
                    pop = upd.split("=")[1]
                if upd.startswith("A="):
                    area = upd.split("=")[1]
                if upd.startswith("C="):
                    cont = upd.split("=")[1]

            # tries to add country, if unsuccessful updates the existing country's information
            if catalogue.addCountry(words[0].strip(), cont, pop, area) is False:
                catalogue.setPopulationOfCountry(words[0].strip(), pop)
                catalogue.setAreaOfCountry(words[0].strip(), area)
                catalogue.setContinentOfCountry(words[0].strip(), cont)

    # saves output file and returns true
    catalogue.saveCountryCatalogue("output")
    return True
