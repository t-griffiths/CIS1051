#hourglass

def topbottom():
    print('|""""""""""|')
    
def sandtop(width):
    lines = width//2 
    for line in range(lines):
        print(" "*(line+1),end="")
        print("\\",end="")
        print("::"*(lines-line),end="")
        print("/",end="")
        print()
        
def middle():
    print("     ||")

def sandbottom(width):
    lines = width//2
    for line in range(lines):
        print(" "*(lines-line),end="")
        print("/",end="")
        print("::"*(line+1),end="")
        print("\\",end="")
        print()

def build():
    topbottom()
    sandtop(8)
    middle()
    sandbottom(8)
    topbottom()

build()


"""
sandtop
line    before   middle
0        1         8 :
1        2         6 :
2        3         4 :
3        4         2 :

n        n+1      
"""
"""
sandbottom
line     before     middle
0          4         2 :
1          3         4 :
2          2         6 :
3          1         8 : 
"""
