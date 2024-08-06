#!/usr/env/python3

import random

def main():
    students = [
        "Amir", "Breana", "Katie", "Clayton", "Coty", "Daiyron",
        "Douglas", "Gabriel", "Jakira", "John", "Jonathan",
        "Justin", "Megan", "Tayo", "Summer", "Tomiwa"]

    # len() function counts up how many names in the list
    headcount = len(students)

    stillChoosing = True

    while(stillChoosing):

        str_number = input(f"Select a number between 1 and {headcount}: ")

        if (len(str_number) == 0):
            int_number = random.randint(1, headcount)
            stillChoosing = False
        elif (int(str_number) > 0 and int(str_number) < 17):
            int_number = int(str_number)
            stillChoosing = False
        else:
            print(f"{str_number} is not a valid choice. Please select a number between 1 and {headcount}.")


    student_choice = students[int_number - 1]

    print(f"{student_choice} is AWESOME!")

main()
