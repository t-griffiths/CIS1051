def checkarmstrong():
    num = int(input("Enter number to check if Armstrong number "))
    total = 0
    x = num

    while x > 0:
        dig = x % 10
        total = total + dig**3
        x = x//10

    if num == total:
        print(str(num) + " is an Armstrong number")
    else:
        print(str(num) + " is not an Armstrong number")

checkarmstrong()
