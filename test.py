import numpy as nu
import tkinter as tk
from pynput.keyboard import Controller,Listener
import time

k = 100
tX = None

#y is reversed
vector = nu.array([[100,100,200],
                 [300,100,200]])
projectedPoint = nu.zeros((2,2))


#new start point
#x
projectedPoint[0][0] = (k*vector[0][0])/(vector[0][2])
#y
projectedPoint[0][1] = (k*vector[0][1])/(vector[0][2])

#new end point
#x
projectedPoint[1][0] = (k*vector[1][0])/(vector[1][2])
#y
projectedPoint[1][1] = (k*vector[1][1])/(vector[1][2])


translation = nu.array([[1,0,0,1],
                       [0,1,0,1],
                       [0,0,1,1],
                       [0,0,0,1]])


def draw(canvas, projectedPoint):
    canvas.delete("all")
    canvas.create_line(projectedPoint[0][0], projectedPoint[0][1], 
                       projectedPoint[1][0],projectedPoint[1][1], 
                       width = 2, fill="black")
    canvas.update()

window = tk.Tk()
window.title("test")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

draw(canvas,projectedPoint)

window.mainloop()