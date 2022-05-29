from turtle import *

class rect:

    def __init__(self , x , y , c , w , h):
        self.x = x
        self.y = y
        self.c = c
        self.w = w
        self.h = h

    def draw_rect(self):
        pu()
        goto(self.x , self.y)
        pd()
        color(self.c)
        begin_fill()
        for i in range(2):
            fd(self.w)
            lt(90)
            fd(self.h)
            lt(90)
        end_fill()


def write_text(x , y , size , c , text):
    pu()
    goto(x , y)
    pd()
    color(c)
    style = ("b tabassom" , size , "bold italic")
    write(text , font = style , align = "center")

def draw_circle(x , y , r , c):
    pu()
    goto(x , y)
    pd()
    color(c)
    begin_fill()
    circle(r)
    end_fill()
    