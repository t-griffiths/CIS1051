#THREE SORT

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your seccond number: "))
num3 = int(input("Enter your third number: "))

if num1<num2 and num1<num3 and num2<num3:
    print (num1)
    print (num2)
    print (num3)

elif num3<num1 and num3<num2 and num2<num1:
    print(num3)
    print(num2)
    print(num1)
    
elif num1<num2 and num1<num3 and num3<num2:
    print(num1)
    print(num3)
    print(num2)

elif num2<num1 and num2<num3 and num3<num1:
    print(num2)
    print(num3)
    print(num1)

elif num3<num2 and num3<num1 and num1<num2:
    print(num3)
    print(num1)
    print(num2)

elif num2<num1 and num2<num3 and num1<num3:
    print(num2)
    print(num1)
    print(num3)

