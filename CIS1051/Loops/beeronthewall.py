

def song():
    x = int(input("Enter an amount of beers on the wall please and thank you "))
    for num in range (x,-1,-1):
        if num > 2:
            print(num, " bottles of beer on the wall, " , num, "bottles of beer")
            print("take one down, pass it around ", num-1 , " bottles of beer on the wall")
        elif num == 2:
            print(num, " bottles of beer on the wall, ", num, " bottles of beer")
            print("take on down pass it around, 1 bottle of beer on the wall")
        elif num == 1:
            print(num, " bottle of beer on the wall ", num, " bottle of beer")
            print("take it down pass it around 0 bottles of beer on the wall")
    


song()
