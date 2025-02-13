import numpy as nu
import tkinter as tk
from pynput.keyboard import Controller,Listener
import time


movementx = 0
movementy = 0
movementz = 0

#vectors original position



#matrix vector math
def translations():
    print()
    #matrix/vector 




#draw vectors

def draw(canvas):
    canvas.delete("all")
    canvas.create_line(200,200,250,250, width = 2, fill="black")
    canvas.update()


    
#input

def input(key):
    try:
        if key.char == 'w':
            movementz += 1
        elif key.char == 's':
            movementz -= 1
        elif key.char == 'a':
            movementx -= 1;
        elif key.char == 'd':
            movementx += 1;
        draw()
    except AttributeError:
        pass




#window
window = tk.Tk()
window.title("Welcome!")



# canvas
canvas = tk.Canvas(window, width=300, height=400)
canvas.pack()



#draw 
draw(canvas)



#listener
listener = Listener(on_press=input())
listener.start()



#refresh window    
window.mainloop()