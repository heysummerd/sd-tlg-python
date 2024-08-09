#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint


AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        
        #print their name or alias
        # get alias data
        aliases = got_dj["aliases"]

        if got_dj["name"] == "":
            print("\n\nName:\nNone\n\nAliases:")
            for alias in aliases:
                print(alias)
        else:
            print("\n\nName:")
            print(got_dj["name"])

        #print affiliated houses
        # get house data
        houses = got_dj["allegiances"]

        print("\nAffiliated Houses:")
        print_data(houses)

        #print list of all books they appear in
        # get book data
        books = got_dj["books"]
        pov_books = got_dj["povBooks"]
        all_books = books + pov_books

        print("\nBook Appearances:")
        print_data(all_books)

def print_data(data):
    if len(data) > 0:
        for item in data:
                result = requests.get(item)
                result_dj = result.json()
                print(result_dj["name"])
    else:
        print("None")





if __name__ == "__main__":
        main()

