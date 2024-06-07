import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Define window boundaries
xmin, ymin = 50, 50
xmax, ymax = 100, 100

# Define a function to compute the region code for a point (x, y)
def compute_code(x, y):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

# Define Cohen-Sutherland line clipping algorithm
def cohen_sutherland_line_clip_and_draw(x0, y0, x1, y1):
    # Compute outcodes
    outcode0 = compute_code(x0, y0)
    outcode1 = compute_code(x1, y1)
    accept = False

    while True:
        if not (outcode0 | outcode1):  # If logical OR is 0, then both points are inside the clip rectangle
            accept = True
            break
        elif outcode0 & outcode1:  # If logical AND is not 0, then both points are outside the clip rectangle
            break
        else:
            # Failed both tests, so calculate the line segment to clip
            # from an outside point to an intersection with clip edge
            x, y = 0, 0  # Initialize coordinates for intersection

            # At least one endpoint is outside the clip rectangle; pick it
            outcode_out = outcode0 if outcode0 else outcode1

            # Find intersection point
            if outcode_out & TOP:  # Point is above the clip rectangle
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif outcode_out & BOTTOM:  # Point is below the clip rectangle
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif outcode_out & RIGHT:  # Point is to the right of the clip rectangle
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif outcode_out & LEFT:  # Point is to the left of the clip rectangle
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            # Now we move outside point to intersection point to clip
            # and get ready for next pass
            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_code(x0, y0)
            else:
                x1, y1 = x, y
                outcode1 = compute_code(x1, y1)

    if accept:
        # Draw the clipped line
        glColor3f(0.0, 1.0, 0.0)  # Green color
        glBegin(GL_LINES)
        glVertex2f(x0, y0)
        glVertex2f(x1, y1)
        glEnd()

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluOrtho2D(0, 500, 0, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)  # Red color

        # Draw the line with red color
        glBegin(GL_LINES)
        glVertex2f(120, 10)
        glVertex2f(40, 130)
        glEnd()

        # Draw the clipping window with green color
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(xmin, ymin)
        glVertex2f(xmax, ymin)
        glVertex2f(xmax, ymax)
        glVertex2f(xmin, ymax)
        glEnd()

        # Perform line clipping and draw the result
        cohen_sutherland_line_clip_and_draw(120, 10, 40, 130)

        pygame.display.flip()
        pygame.time.wait(10)

main()