# EVEN DIGITS

def evendig():
    evendigits = 0
    num = int(input("please enter number "))

    for i in range(len(str(num))):
        digit = num % 10
        if digit % 2 != 1:
            evendigits = evendigits + 1
        num = num // 10
    print(evendigits)

evendig()
