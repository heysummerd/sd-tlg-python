#!/usr/bin/env python3

#imports
import shutil
import os


def main():
    # The following code creates a directory if it does not exist already, and executes this file's code there
    os.chdir("/home/student/mycode/")

    # This code takes an existing file and makes a copy of it (original name, new name)
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # This code takes an existing folder and makes a copy of it (including file contents)
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()

