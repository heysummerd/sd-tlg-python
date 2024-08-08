#!/usr/bin/env python3

# Part 3 - only print out the line if it has the word "vampire" in it!
with open("dracula.txt", "r") as foo:
    file_lines = foo.readlines()
    for line in file_lines:
        if "vampire" in line:
            print(line)


