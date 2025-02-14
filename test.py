import numpy as nu
import tkinter as tk
from pynput.keyboard import Controller,Listener
import time

k = 100
tX = 50
tY = 50
tZ = 50

fovVert = 90
fovHor = 59
aspectRatio = canvas.winfo_width() / canvas.winfo_height()
near = 0
far = 500


#calculate what points can be projected

def fov(canvas, near, far, fovVert, fovHor, np, k):
    windowWidth = canvas.winfo_width()
    windowHeight = canvas.winfo_height()
    fovVert = 2 * (90 - (np.arctan((2 * k) / windowHeight)))
    fovHor = 2 * (90 - (np.arctan((2 * k) / windowWidth)))
    return fovHor, fovVert

def testPointsInView(canvas, near, far, fovVert, fovHor, np, k):
    print()
    #if pointY/X between pointZ cos(fov/2)
    #if pointZ between near and far

def projection(k):
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


    translation = nu.array([[1,0,0,tX],
                        [0,1,0,tY],
                        [0,0,1,tZ],
                        [0,0,0,1]])
    vector1 = nu.array([[[100],[100],[200],[1]],[[150],[150],[250],[1]]])

    newvector = translation @ vector1[1] 
    return projectedPoint







def draw(canvas):
    canvas.delete("all")
    projectedPoint = projection()
    canvas.create_line(projectedPoint[0][0], projectedPoint[0][1], 
                       projectedPoint[1][0],projectedPoint[1][1], 
                       width = 2, fill="black")
    canvas.update()

window = tk.Tk()
window.title("test")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
canvas.winfo_width()
canvas.winfo_height()

draw(canvas)

window.mainloop()