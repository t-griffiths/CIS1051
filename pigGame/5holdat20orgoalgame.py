#HOLD AT 20 OR GOAL GAME
#WORKS

import random
score = 0
turntotal = 0
for x in range(10000):
    while True:
        roll = random.randint(1,6)
        score += roll
        turntotal += roll
        print("roll = ",roll)
        if roll == 1:
            print("Turn total = ",0)
            print("New score = ",score)
            score -= turntotal
            turntotal = 0
            break
        if score > 99:
            print("Turn total = ",turntotal)
            print("New score = ",score)
            turntotal = 0
            break
        if turntotal > 19:
            print("Turn total = ",turntotal)
            print("New score = ",score)
            turntotal = 0
            break
    if score > 99:
        break
    
