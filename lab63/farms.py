#!/usr/bin/env python3


# data
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# Write a for loop that prints each animal from the NE Farm
print("\nPart 1\n")

for animal in farms[0]["agriculture"]:
    print(animal)


# Ask a user to choose a farm (NE, W, SE). Return the plants/animals that
# are raised on that farm
print("\nPart 2\n")

# collect farm choice
farm_choice = input("Which farm would you like to explore? NE, W, or SE?\n>").upper().strip()

# data validation

farm_choice = farm_choice + " Farm"

# print agriculture values from farm choice
for farm in farms:
    if farm["name"] in [farm_choice]:
        for value in farm["agriculture"]:
            print(value)

#Ask a user to choose a farm (NE, W, SE)... but only return ANIMALS from that particular farm
print("\nPart3\n")

# collect farm choice
farm_choice = input("Which farm would you like to explore? NE, W, or SE?\n>").upper().strip()

# data validation

farm_choice = farm_choice + " Farm"

# print agriculture values from farm choice
for farm in farms:
    if farm["name"] in [farm_choice]:
        for value in farm["agriculture"]:
            if value not in ["carrots", "celery"]:
                print(value)



