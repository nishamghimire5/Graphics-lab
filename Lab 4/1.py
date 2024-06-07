import numpy as np
from typing import Tuple
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

Coordinate = Tuple[float, float]

def translate(point: Coordinate, translateX_by: int, translateY_by: int) -> Coordinate:
    x, y = point
    m = np.array([[x], [y], [1]])
    tx_m = np.array([[1, 0, translateX_by], [0, 1, translateY_by], [0, 0, 1]])
    result = np.dot(tx_m, m)
    return tuple(result[:2, 0])

def displayPaint():
    st_point: Coordinate = (-4, -6)
    end_point: Coordinate = (7, 3)
    tsl_By = (5, 8)
    st_tps = translate(st_point, tsl_By[0], tsl_By[1])
    end_tps = translate(end_point, tsl_By[0], tsl_By[1])

    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(st_point[0], st_point[1])
    glVertex2f(end_point[0], end_point[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(st_tps[0], st_tps[1])
    glVertex2f(end_tps[0], end_tps[1])
    glEnd()

def main():
    pg.init()
    pg.display.set_mode((600, 600), DOUBLEBUF | OPENGL | GL_RGB)
    pg.display.set_caption("Translate - COMP342 Computer Graphics Lab")

    gluPerspective(150, 1, 1, 10)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        displayPaint()
        pg.display.flip()

if __name__ == "__main__":
    main()
