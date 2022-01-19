#THOMAS GRIFFITHS
#PIG LATIN

def main():

    vowels=('a','e','i','o','u')
    
    def findFirstVowel(x):
        for i in range(len(x)):
           if x[i] in vowels:
               return i
        return -1    #if no vowels input is given value of -1

    while True:
        userinput = input("Enter your word: ")
        userinput = userinput.lower() # makes lowercase incase input is capital

        if userinput == "done":
            break # break ends program

        word = userinput.split() #splits string into list

        for x in word:
            piglatin = findFirstVowel(x)

            if(piglatin == -1): # if no vowels
                print(x)
            elif(piglatin == 0):
                print (x[1:] + x[0] + "way")
            else:
                print(x[piglatin:] + x[:piglatin] + "ay")

            def reverse():
                print(x[::-1])

            reverse()


main()


