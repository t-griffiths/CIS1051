#SLASH FIGURE

n = int(input("enter integer"))
def slash(width):
    lines = width//2
    for line in range(lines):
        print("\\"*(line*2),end="")
        print("!!"*((width-line*2)-1),end="")
        print("/"*(line*2),end="")
        print()

slash(n*2)



"""
line     before    middle
0          0        14 !  
1          2        10 !
2          4         6 !
3          6         2 !
"""
