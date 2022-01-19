#hold at x outcomes
#works kinda

import random

from collections import Counter
x = int(input("enter the maximum hold value"))
y = int(input("enter amount of runs: "))
print("Score" '\t' "estimated probibility")
scoreValue = [x]

for i in range (0,y):
    holdValue = x
    turnTotal = 0
    score = 0
    count = Counter(scoreValue)

    while True:
        roll = random.randint(1,6)
        if turnTotal >= x:
            break
        if roll == 1:
            turnTotal = 0
            break
        turnTotal += roll

    score = turnTotal
    scoreValue.append(score)

print((x-x),"\t",count[x-x]/y)
print(x,'\t',count[x]/y)
print(x+1,'\t',count[x+1]/y)
print(x+2,'\t',count[x+2]/y)
print(x+3,'\t',count[x+3]/y)
print(x+4,'\t',count[x+4]/y)
print(x+5,'\t',count[x+5]/y)
