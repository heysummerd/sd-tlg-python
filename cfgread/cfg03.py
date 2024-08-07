#!/usr/bin/env python3

# collect file name to read
file_name = input("Please provide a file name to read: ")

## create file object in "r"ead mode
with open(file_name, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    line_count = 0
    for line in configlist:
        line_count += 1

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(f"# of lines: {line_count}")

