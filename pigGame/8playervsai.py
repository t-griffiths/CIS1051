#AI jawn
#WORKS

import random
turns = 0
turns2 = 0
turntotal = 0
turntotal2 = 0
player1score = 0
player2score = 0
while player1score < 100 and player2score < 100:
    while True:
        option = input("Player 1: Roll or Hold")
        option = option.lower()
        if option == "hold":
            break
        else:
            roll = random.randint(1,6)
            if roll == 1:
                turntotal = 0
                turns += 1
                print("Roll = ",roll)
                print("Player 1 score: ",player1score)
                print("Turn total = ",turntotal)
                break
            if turntotal > 19:
                break
            
            player1score += roll
            print("Roll = ",roll)
            turns += 1
        print("Player 1 score = ",player1score)

    while True:
        print("player 2: roll or hold")
        compoption = random.choices(["hold","roll"],[0.45,0.65])
        if compoption == "hold":
            break
        else:
            roll = random.randint(1,6)
            if roll == 1:
                turntotal2 = 0
                turns2 += 1
                print("Roll = ",roll)
                print("Player 2 score: ",player2score)
                print("Turn total = ",turntotal2)
                break
            if turntotal2 > 19:
                break
            
            player2score += roll
            print("Roll = ",roll)
            turns2 += 1
        print("Player 2 score = ",player2score)


