import numpy as np
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
aspectRatio = 16/9
near = 0
far = 500

#square example
vectorRight = nu.array([[[100], [100], [100], [1]], [[100],[0],[100],[1]]])
vectorLeft = nu.array([[[-100], [100], [100], [1]], [[-100],[0],[100],[1]]])
vectorBottom = nu.array([[[100], [200], [100], [1]], [[300],[200],[100],[1]]])
vectorTop = nu.array([[[-100], [100], [100], [1]], [[100],[100],[100],[1]]])


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

def projection(k, vectorBottom,canvas):
    #y is reversed
    vector = vectorBottom
    projectedPoint = nu.zeros((2,4,1))
    projection = nu.array([[k,0,0,0],
                         [0,k,0,0],
                         [0,0,1,0],
                         [0,0,1,0]])
    for i in range(2):
        projectedPoint[i] = projection @ vector[i]
        projectedPoint[i][0][0] = projectedPoint[i][0][0] / vector[i][2][0]
        projectedPoint[i][1][0] = projectedPoint[i][1][0] / vector[i][2][0]
    canvas.create_line(projectedPoint[0][0][0], projectedPoint[0][1][0],
                       projectedPoint[1][0][0],projectedPoint[1][1][0], 
                        width = 2, fill="black")

def translation(tX,tY,tZ):
    translationMatrix = nu.array([[1,0,0,tX],
                                  [0,1,0,tY],
                                  [0,0,1,tZ],
                                  [0,0,0,1]])
    vector1 = nu.array([[[100],[100],[200],[1]],[[150],[150],[250],[1]]])

    newpoint = translationMatrix @ vector1[1]

translation(tX,tY,tZ)

def rotation(vector):
    x = vector[0][0][0]
    y = vector[0][1][0]
    z = vector[0][2][0]
    r = np.sqrt((x ** 2) + (y ** 2) + (z ** 2))
    dVertAngle = 10
    dHorAngle = 20
    vertAngle = np.arccos(-r / z)
    horAngle = np.atan2(y,x)
    translatedAngleVert = vertAngle + dVertAngle
    translatedAngleHor = horAngle + dHorAngle
    tX = r * np.sin(translatedAngleVert) * np.cos(translatedAngleHor)
    tY = r * np.sin(translatedAngleVert) * np.sin(translatedAngleHor)
    tZ = -r * np.cos(translatedAngleVert)
    angleRotationTranslation = nu.array([[1,0,0,tX],
                                         [0,1,0,tY],
                                         [0,0,1,tZ],
                                         [0,0,0,1]])
    newpoint = angleRotationTranslation @ vector[0]

rotation(vectorTop)


def draw(k, vectorBottom, canvas):
    canvas.delete("all")
    projection(k, vectorBottom, canvas)
    canvas.update()

window = tk.Tk()
window.title("test")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()
canvas.winfo_width()
canvas.winfo_height()

draw(k, vectorBottom, canvas)

window.mainloop()