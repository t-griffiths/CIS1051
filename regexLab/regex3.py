#THOMAS GRIFFITHS
#REGEX 3
#MUST ENTER PASSWORD INTO FUNCTION IN SHELL


import re

password = input("Enter valid password")
print("Run password in validpassword() function")

def checklength(password):
    length = re.compile(r".{8,}")
    if not length.search(password):
        return False
    return True

def upcase(password):
    upper = re.compile(r".*[A-Z]+.*")
    if not upper.search(password):
        return False
    return True

def lowcase(password):
    lower = re.compile(r".*[a-z]+.*")
    if not lower.search(password):
        return False
    return True

def checkdigit(password):
    dig = re.compile(r".*\d+.*")
    if not dig.search(password):
        return False
    return True

def validpassword(password):
    if not checklength(password):
        print("Password is invalid. Must contain at least 8 characters")
        return False
    if not upcase(password):
        print("Password is invalid. Must contain at least one upper case letter")
        return False
    if not lowcase(password):
        print("Password is invalid. Must contain at least one lower case letter")
        return False
    if not checkdigit(password):
        print("Password is invalid. Must contain at least one digit.")

    print(password, "is a valid password")
