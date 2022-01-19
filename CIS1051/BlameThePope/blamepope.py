date = input("please enter date ")

month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:]) 

def isLeapYear(year):
    if year % 4 == 0:
            if year % 100 == 0 and not (year % 400 == 0):
                return False
            else:
                return True
    else:
        return False
    
if month == 4 or month == 6 or month == 9 or month == 11:
    if 1 <= day  <= 30:
        print("Valid Date")
    else: print("Invalid Date")
elif month == 1 or month == 5 or month == 7 or month == 8 or month == 9 or month == 12:
    if 1 <= day <= 31:
             print("Valid Date")
    else: print("Invalid Date due to day")

                      
elif month == 2:
    if 1 <= day <= 28:
             print("Valid Date")
    elif day == 29 and isLeapYear(year):
        print("Valid Date")
    else:
        print("Invalid Day")

else:print("Invalid Date due to month")

again = input("Again?")
if again == "no" or again == "n":
    done = True
