import numpy as nu
import tkinter as tk
from pynput.mouse import Listener
import keyboard as kb
import time as t
import threading

#Distance from plane
k = 100

#rotation on axis
rotationX = None
rotationY = None
rotationZ = None

#Might be wrong
#vectors original position
#possible fix
vectorCube = nu.array([
    [[[-50],[-50],[25],[1]],[[50],[-50],[25],[1]]],
    [[[-50],[50],[25],[1]],[[50],[50],[25],[1]]],
    [[[-50],[-50],[25],[1]],[[-50],[50],[25],[1]]],
    [[[50],[-50],[25],[1]],[[50],[50],[25],[1]]],
    [[[-75],[-50],[125],[1]],[[25],[-50],[125],[1]]],
    [[[-75],[50],[125],[1]],[[25],[50],[125],[1]]],
    [[[-75],[-50],[125],[1]],[[-75],[50],[125],[1]]],
    [[[25],[-50],[125],[1]],[[25],[50],[125],[1]]],
    [[[-50],[-50],[25],[1]],[[-75],[-50],[125],[1]]],
    [[[50],[-50],[25],[1]],[[25],[-50],[125],[1]]],
    [[[-50],[50],[25],[1]],[[-75],[50],[125],[1]]],
    [[[50],[50],[25],[1]],[[25],[50],[125],[1]]]
])


#matrix vector math
def translations(vectorCube,tX, tY, tZ):
    translationMatrix = nu.array([[1, 0, 0, tX],
                                  [0, 1, 0, tY],
                                  [0, 0, 1, tZ],
                                  [0, 0, 0, 1]])
    for i, vector in enumerate(vectorCube):
        vector1 = vector
        newvector = nu.zeros((2,4,1))
        newvector = translationMatrix @ vector1
        vectorCube[i] = newvector
    return vectorCube

def rotations(vectorCube,dVertAngle,dHorAngle):
    for i, vector in enumerate(vectorCube):
        x = vector[0][0][0]
        y = vector[0][1][0]
        z = vector[0][2][0]
        r = nu.sqrt((x ** 2) + (y ** 2) + (z ** 2))
        vertAngle = nu.arccos(-r / z)
        horAngle = nu.atan2(y, x)
        translatedAngleVert = vertAngle + dVertAngle
        translatedAngleHor = horAngle + dHorAngle
        tX = r * nu.sin(translatedAngleVert) * nu.cos(translatedAngleHor)
        tY = r * nu.sin(translatedAngleVert) * nu.sin(translatedAngleHor)
        tZ = -r * nu.cos(translatedAngleVert)
        angleRotationTranslation = nu.array([[1, 0, 0, tX],
                                             [0, 1, 0, tY],
                                             [0, 0, 1, tZ],
                                             [0, 0, 0, 1]])
        newVector = angleRotationTranslation @ vector
        vectorCube[i] = newVector
    return vectorCube

def projection(vector):
    # y is reversed
    projectedVector = nu.zeros((2, 4, 1))
    projection = nu.array([[k, 0, 0, 0],
                           [0, k, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 1, 0]])
    for i in range(2):
        projectedVector[i] = projection @ vector[i]
        projectedVector[i][0][0] = projectedVector[i][0][0] / vector[i][2][0]
        projectedVector[i][1][0] = projectedVector[i][1][0] / vector[i][2][0]
        #works only for this graph
        projectedVector[i][0][0] += 300
        projectedVector[i][1][0] += 300
    # canvas.create_line(projectedVector[0][0][0], projectedVector[0][1][0],
    #                    projectedVector[1][0][0], projectedVector[1][1][0],
    #                    width=2, fill="black")
    return projectedVector

def applyVectors(vectorCube):
    vectorsToDraw = nu.zeros((12,2, 4, 1))
    for i, vector in enumerate(vectorCube):
        vectorsToDraw[i] += projection(vector)
    return vectorsToDraw
    
#draw vectors
def draw(canvas, vectorCube):
    canvas.delete("all")
    vectors = applyVectors(vectorCube)
    for i, vector in enumerate(vectors):
        canvas.create_line(vector[0][0][0],vector[0][1][0],vector[1][0][0],vector[1][1][0], width = 2, fill="black")
    canvas.pack()
    canvas.update()

#input
def input(canvas,vectorCube):
    while True:
        try:
            if kb.is_pressed('w'):
                tX = 0
                tY = 0
                tZ = -3
                vectorCube = translations(vectorCube,tX, tY, tZ)
            elif kb.is_pressed('a'):
                tX = 3
                tY = 0
                tZ = 0
                vectorCube = translations(vectorCube,tX, tY, tZ)
            elif kb.is_pressed('s'):
                tX = 0
                tY = 0
                tZ = 3
                vectorCube = translations(vectorCube,tX, tY, tZ)
            elif kb.is_pressed('d'):
                tX = -3
                tY = 0
                tZ = 0
                vectorCube = translations(vectorCube,tX, tY, tZ)
            draw(canvas, vectorCube)
        except AttributeError:
            pass
        t.sleep(.01)

def mouse(vectorCube, canvas, x, y):
    global mousePosition
    try:
        dx = x - mousePosition[0] if mousePosition[0] is not None else 0
        dy = y - mousePosition[1] if mousePosition[1] is not None else 0
        if dx > 0:
            dVertAngle = 0
            dHorAngle = 1
            vectorCube = rotations(vectorCube, dVertAngle, dHorAngle)
        if dx < 0:
            dVertAngle = 0
            dHorAngle = -1
            vectorCube = rotations(vectorCube, dVertAngle, dHorAngle)
        if dy < 0:
            dVertAngle = -1
            dHorAngle = 0
            vectorCube = rotations(vectorCube, dVertAngle, dHorAngle)
        if dy > 0:
            dVertAngle = 1
            dHorAngle = 0
            vectorCube = rotations(vectorCube, dVertAngle, dHorAngle)
        draw(canvas, vectorCube)
        mousePosition = (x, y)
    except AttributeError:
        pass

#window
window = tk.Tk()
window.title("Welcome!")

# canvas
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

#draw 
draw(canvas, vectorCube)

#listener
listenerMouse = Listener(on_move=lambda x, y: mouse(vectorCube, canvas, x, y))
listenerMouse.start()
input(canvas,vectorCube)


thread = threading.Thread(target=input, args=(canvas, vectorCube))
thread.daemon = True
thread.start()

#refresh window
window.mainloop()
