from random import *
from turtle import *
from lib import *


title("Hangman")
bgcolor("tomato")
ht()
speed(0)

b1 = rect(-150 , 37.5 , "limegreen" , 300 , 75)
b2 = rect(-100 , -25 , "limegreen" , 200 , 50)
b3 = rect(-300 , 250 , "cyan" , 100 , 25)

def menu_buttons():
    b1.draw_rect()
    b2.draw_rect()
    write_text(0 , 50 , 36 , "red" , "Start")
    write_text(0 , -12.5 , 24 , "red" , "Exit")

menu_buttons()

names = ["elephant" , "wolf" , "cat" , "dog" , "cow" , "horse" , "goat"
         , "duck" , "aligator" , "crow" , "tiger" , "lion" , "panther"
         , "leopard" , "cheetah" , "penguin" , "rhinoceros" , "hippopotamus"
         , "snake" , "eagle" , "salmon"]

name = choice(names)
b = ["-"] * len(name)

def main():
    w = 0
    a = "-" * len(name)
    b3.draw_rect()
    
    write_text(-250 , 250 , 16 , "black" , "Back")
    write_text(0 , 250 , 36 , "black" , "chances :")
    write_text(0 , 200 , 36 , "black" , len(name) - w)
    write_text(0 , 0 , 72 , "black" , a)

    while True:
        s = str()
        x = textinput("Guess Box" , "Enter a character")
        undo()

        for i in range(len(name)):
            if x == name[i]:
                b[i] = x
        
        if name.count(x) == 0:
            w = w + 1
            draw_circle(0 , 150 , 50 , "tomato")
            write_text(0 , 200 , 36 , "black" , len(name) - w)
            
        for i in b:
            s = s + i

        write_text(0 , 0 , 72 , "black" , s)

        if b.count("-") == 0:
            break

        if w == len(name):
            break
        
        listen()

    clear()

    bgcolor("khaki")
    t = "The answer is : " + name

    if w < len(name):
        write_text(0 , 0 , 96 , "cyan" , "You Win!!!")
        write_text(0 , -100 , 36 , "cyan" , t)
    else:
        write_text(0 , 0 , 96 , "cyan" , "You Lose!!!")
        write_text(0 , -100 , 36 , "cyan" , t)



class button(rect):

    def __init__(self, x, y, c, w, h):
        super().__init__(x, y, c, w, h)

    def clicked(x , y): 
        if x > -150 and x < 150:
            if y > 37.5 and y < 107.5:
                clear()
                main()
                

        if x > -100 and x < 100:
            if y > -25 and y < 25:
                bye()
        
        if x > -300 and x < -200:
            if y > 250 and y < 275:
                clear()
                menu_buttons()


onscreenclick(button.clicked)
listen()
mainloop()
