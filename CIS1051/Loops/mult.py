#TIMES TABLE

def table():
    num = input("enter integer ")
       
    for x in range(1,int(num)+1):
        for y in range(1,int(num)+1):
            print(x * y, end = "\t")
        print(' ')


table()

