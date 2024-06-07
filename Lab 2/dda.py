from typing import Tuple 
import pygame as pg 
from pygame import display, event 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 

def DDA(start_coordinate: Tuple[int, int], end_coordinate: Tuple[int, int]) -> list[Tuple[float, float]]:
    x1, y1 = start_coordinate 
    x2, y2 = end_coordinate 

    dx = x2 - x1 
    dy = y2 - y1 

    steps = max(abs(dx), abs(dy)) 

    Xinc = dx / steps 
    Yinc = dy / steps 

    X = x1 
    Y = y1 
    vertices: list[Tuple[float, float]] = [] 

    for i in range(steps): 
        vertices.append((X, Y)) 
        X = X + Xinc 
        Y = Y + Yinc 
    return vertices 

def drawDDA():
    vertices = DDA((400, 100), (100, 450))
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for v in vertices:
        x, y = v 
        glVertex2f(x, y) 
    glEnd()
    glFlush()

def main():
    pg.init()
    display.set_mode((500, 500), DOUBLEBUF | OPENGL | GL_RGB)
    display.set_caption("DDA - Nisham Ghimire")
    gluOrtho2D(0, 500, 0, 500)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()
        drawDDA()
        display.flip()

main()