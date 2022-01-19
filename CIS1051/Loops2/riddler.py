#THE RIDDLER
# all four digets are different
# digit in the thousands place is 3 x digit in tens
# number is odd
# sum of digits is 27

def riddle():
    total = 0 #adress
    num1 = 0 #thousands
    num2 = 0 #hundreds
    num3 = 0 #tens
    num4 = 0 #ones

    for total in range(1000,10000):
        num1 = (total // 1000)
        num2 = (total // 100) % 10
        num3 = (total //10) % 10
        num4 = total % 10
    
        if (num1 != num2) and (num1 != num3) and (num1 != num4) and (num2 != num3) and (num2 != num4) and (num3 != num4):
            if num1 == (3*num3):
                if num4 % 2 == 1:
                    if num1 + num2 + num3 + num4 == 27:
                        print("The address is " + str(num1) + str(num2) + str(num3) + str(num4) + " Pennsylvania Ave.")


riddle()


