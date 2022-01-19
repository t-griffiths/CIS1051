#VOWEL COUNT

def checkvowels():
    word = input("please enter a word/combination of letters ")
    vowels = 0

    for x in word:
        if (x == "a" or x =="e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U"):
            vowels = vowels+1

    print(vowels)

checkvowels()
