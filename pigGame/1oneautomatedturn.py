#ONE AUTOMATED TURN
#THOMAS GRIFFITHS
#WORKS PERFECT

import random
turns = 0
turntotal = 0
while True:
    roll = random.randint(1,6)
    if roll == 1:
        turntotal = 0
        turns += 1
        print("Roll = ",roll)
        print("Turn total = ",turntotal)
        break
    else:
        turntotal += roll
        turns += 1
        print("Roll = ",roll)
        print("Turn total = ",turntotal)
    if turntotal > 19:
        break
