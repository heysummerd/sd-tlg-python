#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
posts = 0 # counter for successful posts

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # create dictionary for failed logins / associated IPs
    fail_IPs = {}

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            fail_IPs[loginfail] = line.split(" ")[-1].rstrip()
        elif "POST" in line:
            posts += 1 

print("The number of failed log in attempts is", loginfail)
print(f"Here is the fail log:\n{fail_IPs}")
print("\nThe number of successful posts is", posts)
