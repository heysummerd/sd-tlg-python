#!/usr/bin/env python3

# imports
import shutil
import os


def main():
    # change directory
    os.chdir('/home/student/mycode/')

    # move fileA to destinationB
    shutil.move('raynor.obj', 'ceph_storage/')

    # collect new file name from user
    xname = input("What is the new name for kerrigan.obj? ")

    # rename the new file
    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)

if __name__ == "__main__":
    main()

