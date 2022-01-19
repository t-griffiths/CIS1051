def checkword(validchars, word):
    for x in word:
        x = x.lower()
        if validchars.count(x) == 0:
            print(x, " is not a valid hawaiian character")
            return False
        return True

def combine(word):
    result = ""
    i = 0

    while i < len(word) - 1:
        x = word[i]
        x = x.lower()

        if x == "a":
            nextletter = word[i+1]
            nextletter = nextletter.lower()

            if nextletter == "i":
                result += "eye-"
                i +=1
            elif nextletter == "e":
                result += "eye-"
                i +=1
            elif nextletter == "o":
                result += "ow-"
                i +=1
            elif nextletter == "u":
                result += "ow-"
                i +=1
            else:
                result +="ah-"
        elif x == "e":
            nextletter = word[i+1]
            nextletter = nextletter.lower()

            if nextletter == "i":
                result += "ay-"
                i+=1
            elif nextletter == "u":
                result += "ehoo-"
            else:
                result += "eh-"

        elif x == "i":
            nextletter = word[i+1]
            nextletter = nextletter.lower()

            if nextletter == "u":
                result += "ew-"
                i += 1
            else:
                result+= "ee-"
        elif x == "o":
            nextletter = word[i+1]
            nextletter = nextletter.lower()

            if nextletter == "i":
                result += "oyo-"
                i += 1
            elif nextletter == "u":
                result += "ow-"
                i += 1
            else:
                result += "ah-"

        elif x == "u":
            nextletter = word[i+1]
            nextletter = nextletter.lower()

            if nextletter == "i":
                result += "ooey-"
            else: result += "oo-"

        elif x == " " and result[len(result)-1] == "-":
            result = result[0:len(result) - 1]+ "-"

        elif x == "\"" and result[len(result)-1] == "-":
            result = result[0:len(result) - 1]+ "-"
        else:
            result += x

        i += 1

    if i < len(word):
        x = word[len(word) - 1]
        x = x.lower()

        if x == "a" or x == "e" or x == "o":
            result = result + x + "h"
        elif x == "i":
            result += "ee"
        elif x == "u":
            result += "oo"
        else:
            result += x

    if result[len(result)-1] == "-":
        result = result[0:len(result)-1]

    result = result.capitalize()
    return result

if __name__=="__main__":

    validchars = ["a","e","i","o","u","p","k","h","l","m","n","w","\'"]

    while True:
        word = input("enter hawaiin word")
        if (checkword(validchars,word)):
            word = word.strip()
            result = combine(word)

            word = word.upper()
            print(word)
            print(result)
        askagain = input("do you want to find the pronounciation for another word?")
        askagain = askagain.upper()

        if askagain != "Y" and askagain != "YES":
            break
        
    
    
