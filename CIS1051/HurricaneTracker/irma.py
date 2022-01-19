import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
   
    (t, wn, map_bg_img) = irma_setup()
   
    file = open("data/irma.csv")
    read = file.readlines() # puts lines from csv in list
    
    for i in range(1,len(read)):
        line = read[i] #gets numbered line for each iteration
        splitline = line.split(",")
        latitude = float(splitline[2])
        longitude = float(splitline[3])
        wind = float(splitline[4])

        if wind < 73:
            category = 0
            t.color("white")
            t.pensize(1)
        elif wind > 73 and wind < 96:
            category = 1
            t.color("blue")
            t.pensize(2)
        elif wind > 95 and wind < 111:
            category = 2
            t.color("green")
            t.pensize(3)
        elif wind > 110 and wind < 130:
            category = 3
            t.color("yellow")
            t.pensize(4)
        elif wind > 129 and wind < 157:
            category = 4
            t.color("orange")
            t.pensize(5)
        elif wind > 156:
            category = 5
            t.color("red")
            t.pensize(6)
        t.goto(longitude,latitude)
        t.write(str(category))
    turtle.Screen().exitonclick()

if __name__ == "__main__":
    irma()
