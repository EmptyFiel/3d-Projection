import numpy as nu
import tkinter as tk
from pynput.keyboard import Controller,Listener
import time

#translations
movementX = 0
movementY = 0
movementZ = 0

#Distance from plane
distance = 100

#rotation on axis
rotationX = None
rotationY = None
rotationZ = None


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
            movementZ += 1
        elif key.char == 's':
            movementZ -= 1
        elif key.char == 'a':
            movementX -= 1
        elif key.char == 'd':
            movementX += 1
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