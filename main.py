import numpy as nu
import tkinter as tk
from pynput.keyboard import Controller,Listener

VectorCube = nu.array([
    [[[25],[25],[25],[1]],[[125],[25],[25],[1]]],
    [[[25],[125],[25],[1]],[[125],[125],[25],[1]]],
    [[[25],[25],[25],[1]],[[25],[125],[25],[1]]],
    [[[125],[25],[25],[1]],[[125],[125],[25],[1]]],
    [[[25],[25],[125],[1]],[[125],[25],[125],[1]]],
    [[[25],[125],[125],[1]],[[125],[125],[125],[1]]],
    [[[25],[25],[125],[1]],[[25],[125],[125],[1]]],
    [[[125],[25],[125],[1]],[[125],[125],[125],[1]]],
    [[[25],[25],[25],[1]],[[25],[25],[125],[1]]],
    [[[125],[25],[25],[1]],[[125],[25],[125],[1]]],
    [[[25],[125],[25],[1]],[[25],[125],[125],[1]]],
    [[[125],[125],[25],[1]],[[125],[125],[125],[1]]]
])

def function():
    test.testprint()

function()

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
    
def rotations():
    print()




#draw vectors

def draw(canvas):
    canvas.delete("all")
    canvas.create_line(200,200,250,250, width = 2, fill="black")
    canvas.update()


    
#input

def input(key):
    try:
        if key.char == 'w':
            print()
        elif key.char == 's':
            print()
        elif key.char == 'a':
            print()
        elif key.char == 'd':
            print()
        draw(canvas)
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
listener = Listener(on_press=input(key))
listener.start()



#refresh window    
window.mainloop()
