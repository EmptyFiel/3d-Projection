import numpy as nu
import tkinter as tk
from pynput.mouse import Listener
import keyboard as kb
import time as t

#mouse position and direction
mousePosition = (None,None)

#translations
tX = 0
tY = 0
tZ = 0

#Distance from plane
k = 100

#rotation on axis
rotationX = None
rotationY = None
rotationZ = None


#vectors original position
vectorCube = nu.array([
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



#matrix vector math
def translations():
    translationMatrix = nu.array([[1, 0, 0, tX],
                                  [0, 1, 0, tY],
                                  [0, 0, 1, tZ],
                                  [0, 0, 0, 1]])
    vector1 = nu.array([[[100], [100], [200], [1]], [[150], [150], [250], [1]]])
    newvector = nu.zeros((2,4,1))
    for i in range(2):
        newvector[i] = translationMatrix @ vector1[i]

# def rotations():
#     x = vector[0][0][0]
#     y = vector[0][1][0]
#     z = vector[0][2][0]
#     r = nu.sqrt((x ** 2) + (y ** 2) + (z ** 2))
#     dVertAngle = 10
#     dHorAngle = 20
#     vertAngle = nu.arccos(-r / z)
#     horAngle = nu.atan2(y, x)
#     translatedAngleVert = vertAngle + dVertAngle
#     translatedAngleHor = horAngle + dHorAngle
#     tX = r * nu.sin(translatedAngleVert) * nu.cos(translatedAngleHor)
#     tY = r * nu.sin(translatedAngleVert) * nu.sin(translatedAngleHor)
#     tZ = -r * nu.cos(translatedAngleVert)
#     angleRotationTranslation = nu.array([[1, 0, 0, tX],
#                                          [0, 1, 0, tY],
#                                          [0, 0, 1, tZ],
#                                          [0, 0, 0, 1]])
#     newVector = angleRotationTranslation @ vector[0]

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
    canvas.update()


#input

def input(canvas):
    while True:
        try:
            if kb.is_pressed('w'):
                print()
            elif kb.is_pressed('a'):
                print()
            elif kb.is_pressed('s'):
                print()
            elif kb.is_pressed('d'):
                print()
            draw(canvas, vectorCube)
        except AttributeError:
            pass
        t.sleep(.01)

def mouse(mousePosition, x, y):
    try:
        dx =  x - mousePosition[0]
        dy = y - mousePosition[1]
        mousePosition = (x, y)
    except AttributeError:
        pass


#window
window = tk.Tk()
window.title("Welcome!")



# canvas
canvas = tk.Canvas(window, width=300, height=400)
canvas.pack()



#draw 
draw(canvas, vectorCube)



#listener
# listenerMouse = Listener(on_move=mouse(mousePosition))
# listenerMouse.start()
# input(canvas)

#refresh window    
window.mainloop()
