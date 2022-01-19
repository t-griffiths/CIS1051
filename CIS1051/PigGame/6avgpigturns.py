#AVERAGE PIG TURNS
#IT WORKS YEET
#THOMAS GRIFFITHS


def avgpigturns():
    import random
    games = input("number of games?")
    games = int(games)
    holder = {}
    for i in range(games):
        total = 0
        score = 0
        turntotal = 0
        while total < 99:
            while True:
                roll = random.randint(1,6)
                total += roll
                score += roll
                if roll == 1:
                    total = total - score
                    score = 0
                    turntotal = turntotal + 1
                    break
                if total > 99:
                    score = 0
                    turntotal = turntotal + 1
                    break
                if score > 19:
                    score = 0
                    turntotal = turntotal + 1
                    break
        if turntotal not in holder:
            holder[turntotal] = 1
        else:
            holder[turntotal] = holder[turntotal]+1

    nums = 0
    for key in sorted(holder.keys()):
        product = key*holder[key]
        nums = nums+product
    print("Avg turns: ",nums/games)

avgpigturns()
