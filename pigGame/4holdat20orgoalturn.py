#HOLD AT 20 OR GOAL TURN
#WORKS PERFECT YEET
#THOMAS GRIFFITHS




import random
score = int(input("Enter score "))
turntotal = 0
while True:
    roll = random.randint(1,6)
    score += roll
    turntotal += roll
    print("roll: ",roll)
    if roll == 1:
        print("Turn total = 0")
        score = 0
        print("New score = ",score)
        break
    if score > 99:
        print("Turn total = ",turntotal)
        print("New score = ",score)
        break
    if turntotal > 19:
        print("Turn total = ",turntotal)
        print("New score = ", score)
        break
        


