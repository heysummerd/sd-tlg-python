#!/usr/bin/env python3

# Part 5 - only print out the line if it has the word "vampire" in it!
# REGARDLESS of case
# How many lines is that?
with open("dracula.txt", "r") as foo:
    file_lines = foo.readlines()
    vamp_line_count = 0

    for line in file_lines:
        if "vampire".casefold() in line.casefold():
            vamp_line_count += 1
            print(line)
    
    print(f"\nLine count: {vamp_line_count}")
