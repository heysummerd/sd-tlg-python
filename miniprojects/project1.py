#!/usr/bin/env python3

# DONUT BAKERY: What will happen in your dream tonight, based on the donut you construct?

# imports
import os
import time

# main function

def main():

    again = True

    while again:
        welcome()
        base = select_base()
        filling = select_filling()
        icing = select_icing()
        topping = select_topping()
        scores = [base, filling, icing, topping]
        score = sum(scores)
        analyze_dreams(score)
        again = again()
    
    clear()
    print("\n\nThank you for visiting Donut Fear Bakery! We hope you end up having a great night's sleep.")
    exit_program()

# time delay
def pause():
    time.sleep(2)

# exit program
def exit_program():
    print("\n\nLeaving the kitchen...\n\n")
    sleep()
    sys.exit(0)

# clear screen
def clear():
    os.system("clear")

# welcome
def welcome():
    print("\n\nWelcome to Donut Fear Bakery!\n\nPast these doors, you will be able to construct a unique donut.\n\nOnce baked, our special Donut Dream Machine will analyze the results...\nand predict what will happen in your dreams tonight!\n\n")
    
    proceed = input("Are you ready to proceed? [Y/N]\n>")

    # validate answer
    while proceed.lower().strip() not in ['y', 'n']:
        print("Please respond by entering 'Y' to proceed or 'N' to leave")
        proceed = input("\nAre you ready to proceed? [Y/N]\n>")
    
    if proceed.lower().strip() in ['n']:
        print("\n\nWe understand - donut dream predictions are not for everyone.\nCome back when you are ready!")
        exit_program()

    # clear screen
    clear()

    # Enter kitchen
    print("You have entered the bakery kitchen! Grab an apron and let's get started.\n\n")

# select ingredient function
def select_ingredient(ingredient, options):
    
    # print ingredient menu
    print(f"Please select your {ingredient} by entering its # on the menu shown below:  \n")

    for option in options:
        print(f"{option} = {options[option]}")

    # ask for a selection
    selection = input(f"\n\nSelection: # ")

    # clear screen
    clear()

    # return the selection
    return selection



# select donut base
def select_base():

    # base ingredients
    base_options = {
        1:"vanilla",
        2:"chocolate",
        3:"blueberry",
        4:"strawberry"
            }
    
    # call select_ingredient function
    base = select_ingredient("base", base_options)

    # collect and return the selected base ingredient
    return int(base)
    

# select donut filling
def select_filling():

    # filling ingredients
    filling_options = {
        1:"no filling",
        2:"custard",
        3:"raspberry jam",
        4:"apple crisp"
            }

    # call select_ingredient function
    filling = select_ingredient("filling", filling_options)

    # collect and return the selected base ingredient
    return int(filling)


# select donut icing
def select_icing():

    # icing ingredients
    icing_options = {
        1:"no icing",
        2:"regular glaze",
        3:"chocolate glaze",
        4:"maple glaze"
            }

    # call select_ingredient function
    icing = select_ingredient("icing", icing_options)

    # collect and return the selected base ingredient
    return int(icing)

# select donut topping
def select_topping():

    # topping ingredients
    topping_options = {
        1:"no topping",
        2:"sprinkles",
        3:"chopped nuts",
        4:"mini m&ms"
            }

    # call select_ingredient function
    topping = select_ingredient("topping", topping_options)

    # collect and return the selected base ingredient
    return int(topping)

# generate dream results
def analyze_dreams(score):
    # simulate a loading screen
    i = 1;
    while i < 3:
        clear()
        print("\n\nYour donut is being analyzed....")
        pause()
        i += 1

    # select dream result
    clear()
    print("\n\n")
    if score < 5:
        print("A small woodland creature will lead you to a meadow")
    elif score < 7:
        print("A childhood friend will save you from a grave fate")
    elif score < 9:
        print("You will catch a glimpse of the year 3333")
    elif score < 11:
        print("A million-dollar idea will come to you")
    elif score < 13:
        print("You will shed a heavy feeling and wake up refreshed")
    elif score < 15:
        print("You will attend a black tie event while undercover")
    else:
        print("You will not have any dreams tonight!")
    print("\n\n\n")

# make another or exit
def again():
    answer = input("\n\n Sensational! Would you like to craft another donut? [Y/N]\n>")

    while answer.lower().strip() not in ['y', 'n']:
        print("Not a valid response - please enter 'Y' for 'yes' or 'N' for 'no'\n")
        answer = input("\n\nWould you like to craft another donut? [Y/N]\n>")

    if answer.lower().strip() in ['n']:
        return False
    else:
        return True

# call main
main()

