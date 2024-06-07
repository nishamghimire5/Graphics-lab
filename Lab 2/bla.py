import pygame
from pygame import display,event
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def Draw():
    x1, y1, x2, y2 = 200, 50 , 400, 50
    glClear(GL_COLOR_BUFFER_BIT)

    if (x2-x1) == 0:
        M = (y2-y1)
    else:
        M = (y2-y1)/(x2-x1)

    if abs(M) < 1:
        if x1 > x2:
            t = x1
            x1 = x2
            x2 = t

            t = y1
            y1 = y2
            y2 = t

        dx = abs(x2-x1)
        dy = abs(y2-y1)

        p = 2*dy-dx

        x = x1
        y = y1

        glBegin(GL_POINTS)
        while x <= x2:
            glVertex2f(x, y)
            x = x+1

            if p >= 0:
                if M < 1:
                    y = y+1
                else:
                    y = y-1
                p = p+2*dy-2*dx
            else:
                y = y
                p = p+2*dy
        glEnd()

    if abs(M) >= 1:
        if y1 > y2:
            t = x1
            x1 = x2
            x2 = t

            t = y1
            y1 = y2
            y2 = t

        dx = abs(x2-x1)
        dy = abs(y2-y1)

        p = 2*dx-dy

        x = x1
        y = y1

        glBegin(GL_POINTS)
        while y <= y2:
            glVertex2f(x, y)
            y = y+1

            if p >= 0:
                if M >= 1:
                    x = x+1
                else:
                    x = x-1
                p = p+2*dx-2*dy
            else:
                x = x
                p = p+2*dx
        glEnd()

    glFlush()

def main():
    pygame.init()
    display.set_mode((500, 500), pygame.DOUBLEBUF | pygame.OPENGL)
    display.set_caption("BLA - Nisham Ghimire")

    gluOrtho2D(0, 500, 0, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Draw()

        pygame.display.flip()

if __name__ == '__main__':
    main()