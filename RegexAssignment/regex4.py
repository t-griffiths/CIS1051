#REGEX 4
#THOMAS GRIFFITHS

import random
import time

def openfile(filename):
    with open(filename,"r") as infile:
        return [word.strip() for word in infile.readlines()]

def password():
    words = openfile("words.txt")
    fourletters = [word.lower() for word in words if len(word) >= 4 and word.islower()]
    rand = random.sample(fourletters,4)
    print("Creating password with four random lowercase words at least four letters long...")
    time.sleep(2)
    print("New password:","".join(rand))


password()
