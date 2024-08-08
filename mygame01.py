#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# imports
import os
import time
from emoji import emojize

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print(f'''
    RPG Game
    ========
    * Get to the Garden with a key {emojize(":key:")}   and a potion {emojize(":test_tube:")}   to win! Beware of the monsters! {emojize(":alien_monster:")}   *
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    # show move options
    moveOptions()

def moveOptions():
    print("\nMove Options:\n---------------------------")
    for room in rooms[currentRoom]:
        if room != 'item':
            direction = ''
            if room == "east":
                direction = "right"
            elif room == "west":
                direction = "left"
            elif room == "north":
                direction = "up"
            else:
                direction = "down"
            emoji = emojize(":" + direction + "_arrow:")
            print(f'{emoji:<3} {room:<5} : {rooms[currentRoom][room]:<10}')

    print("\n")

def clear():
    os.system("clear")

def pause(seconds):
    time.sleep(seconds)

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                  'west'  : 'Closet',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },
            'Closet' : {
                  'east' : 'Hall',
                  'item' : 'silly hat'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster'
                },
            'Dining Room' : {
                'west' : 'Hall',
                'south': 'Garden',
                'item' : 'potion'
                },
            'Garden' : {
                'north'  : 'Dining Room'
                }
           }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')
        pause(2)

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
        pause(2)

    #if they type 'give' first
    if move[0] == 'give' :
        # check if 'silly hat' is item player wants to give
        # check if 'silly hat' is in inventory
        # check if monster is in room
        if  move[1] == 'silly hat' and 'silly hat' in inventory and'monster' in rooms[currentRoom]['item']:
            clear()
            # display monster's response
            print('''\nYou offer the silly hat to the monster. 
It clutches the hat, places it carefully on its head, and beams. 
                       
You can tell it has found a new lease on life as it scampers out the kitchen window.''')
            # delete monster from the room
            del rooms[currentRoom]['item']
            # delete silly hat from inventory
            inventory.remove("silly hat")
            pause(8)
        else:
            #tell them they can't give it
            print(f"Can't give {move[1]}!")
            pause(2)

    clear()

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        # check if 'silly hat' in inventory
        if 'silly hat' in inventory:
            print('A monster crouches in the corner, eyeing your silly hat hopefully')
        else:
            print('A monster has got you... GAME OVER!')
            break

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
