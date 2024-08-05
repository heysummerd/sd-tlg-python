#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter your favorite movie: ")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me your favorite movie is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me your favorite movie is:", user_input)

    theater_input = input("What is your movie theater of choice? ")
    print(f"You told me your movie theater of choice is: {theater_input}")
                    # f-string
main()

