#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    startdate = "2019-11-11"
    enter_dates = True

    ## update the date below, if you like
    while enter_dates:
        try:
            # ask if they want to enter a start date
            answer = input("Would you like to enter a start date? [Y/N]\n>").lower().strip()
            if answer == 'n':
                enter_dates = False
                break
            elif _answer == 'y':
                    # ask for the start date
                    startdate = input("Enter a start date using format: YYYY-MM-DD:\n>").strip()


    startdate = "start_date=" + startdate

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

