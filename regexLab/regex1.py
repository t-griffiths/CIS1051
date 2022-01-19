#THOMAS GRIFFITHS
#REGEX 

filename = "/Users/thomasgriffiths/Desktop/python/regexassignment/words.txt"
fileopen = open(filename, 'r')
lines = fileopen.readlines()
 
import re

def catordog(): #1
    catcount = 0
    dogcount = 0
    for line in lines:
        if re.search("cat",line): # .search checks for match anywhere in string
            catcount += 1
    for line in lines:
        if re.search("dog",line):
            dogcount += 1

    print(catcount, "words containing cat")
    print(dogcount, "words containing dog")

def fourletter(): #2
    fourcount = 0
    for line in lines:
        if re.search(r'\b\w{4}\b',line):
            fourcount += 1
    print(fourcount, "words with 4 letters")

def findhun(): # 3
    huncount = 0
    for line in lines:
        if re.match("hun",line):
            huncount += 1
    print(huncount, "words containing hun")

def ingorion(): # 4
    ingscount = 0
    for line in lines:
        if re.search(r".ing",line):
            ingscount += 1
    ionscount = 0
    for line in lines:
        if re.search(r".ion",line):
            ionscount += 1

    print(ingscount, "words ending in -ing")
    print(ionscount, "words ending in -ion")

    if ingscount > ionscount:
        print("More words end in -ing")
    else:
        print("More words end in -ion")

def que(): #5
    quecount = 0
    for line in lines:
        if re.search(r"q(?!u)",line): #?! looks ahead and says not followed by
            quecount += 1

    print(quecount, "words containing q not followed by u")

def novowels(): #6 #doesnt work
    novowcount = 0
    vow = re.compile(r"[aeiouAEIOU]")
    for word in lines:
        match = vow.search(word)
        if not vow.search(word):
            novowcount += 1
    print(novowcount, "words containing no vowels")

def onlyvowels(): #7 #doesnt work
    onlyvow = 0
    vow = re.compile(r"^[aeiouAEIOU]+$")
    for word in lines:
        match = vow.search(word)
        if match is not None:
            onlyvow += 1
    print(onlyvow, "words without consenants")

def notcontractions(): #8 
    ntcount = 0
    for line in lines:
        if re.search(r"('nt)",line):
            ntcount += 1

    print(ntcount, "words contracted with not")
    
def twovowsinrow(): # 9 
    twovowcount = 0
    vowelregex = re.compile(r"((a|e|i|o|u){2})")    
    for line in lines:
        if re.search(vowelregex,line):
            twovowcount += 1
    print(twovowcount, " words with two vowels in a row")

def twovows(): # 10
    twovowcount = 0
    vowelregex = re.compile(r"^([^aeiou]*[aeiou]){2,}[^aeiou]*$")    
    for line in lines:
        if re.search(vowelregex,line):
            twovowcount += 1
    print(twovowcount, " words with two vowels")

catordog()
fourletter()
findhun()
ingorion()
que()
novowels()
onlyvowels()
notcontractions()
twovowsinrow()
twovows()
