#!/usr/bin/env python3

# Part 6 - only print out the line if it has the word "vampire" in it!
# REGARDLESS of case
# How many lines is that?
# Write these lines to a second file named vampytimes.txt

with open("dracula.txt", "r") as file1:
    file_lines = file1.readlines()
    vamp_line_count = 0

    with open("vampytimes.txt", "w") as file2:
        for line in file_lines:
            if "vampire".casefold() in line.casefold():
                vamp_line_count += 1
                print(line, file=file2)

    print(f"\nLine count: {vamp_line_count}")
