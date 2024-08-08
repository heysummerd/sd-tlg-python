#!/usr/bin/env python3

# Part 4 - only print out the line if it has the word "vampire" in it!
# REGARDLESS of case
with open("dracula.txt", "r") as foo:
    file_lines = foo.readlines()
    for line in file_lines:
        if "vampire".casefold() in line:
            print(line)
