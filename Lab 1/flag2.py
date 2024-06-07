import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Function to draw a circle using the specified parameters
def draw_circle(x, y, radius, num_segments, n):
    glBegin(GL_TRIANGLE_FAN)
    
    glVertex2f(x, y)  

    for i in range(num_segments + 1):
        theta = n * math.pi * float(i) / float(num_segments)
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)  
        
        glVertex2f(x + dx, y + dy)
    glEnd()

# Function to draw attributes of the flag
def draw_flag_attributes(x, y, radius, num_segments, n):
    draw_circle(x, y, radius, num_segments, n)
    for i in range(num_segments):
        glBegin(GL_TRIANGLES)
        
        theta1 = n * math.pi * float(i) / float(num_segments)
        x1 = x + radius * math.cos(theta1)
        y1 = y + radius * math.sin(theta1)
        theta2 = n * math.pi * float(i + 1) / float(num_segments)
        x2 = x + radius * math.cos(theta2)
        y2 = y + radius * math.sin(theta2)
        
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glVertex2f(((x1 + x2) / 2) + ((x1 + x2 - 2 * x) / 2), ((y1 + y2) / 2) + ((y1 + y2 - 2 * y) / 2))
        glEnd()

# Function to draw the flag of Nepal
def draw_nepal_flag():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Red triangle on top of the flag
        glBegin(GL_TRIANGLES)
        glColor3f(0.8627, 0.0784, 0.2353)
        glVertex2f(0.0, 0.0)
        glVertex2f(0, 0.5)
        glVertex2f(0.75, 0)
        glEnd()

        # Red triangle on the bottom of the flag
        glBegin(GL_TRIANGLES)
        glColor3f(0.8627, 0.0784, 0.2353)
        glVertex2f(0, 0.25)
        glVertex2f(0, -0.5)
        glVertex2f(0.75, -0.50)
        glEnd()

        # Blue quadrilateral on the flag
        glBegin(GL_QUAD_STRIP)
        glColor3f(0.0, 0.2196, 0.5765)
        glVertex2f(0.00, -0.50)
        glVertex2f(0.00, 0.50)
        glVertex2f(-0.045, -0.50)
        glVertex2f(-0.045, 0.575)
        glEnd()

        # Additional blue quadrilaterals on the flag
        glBegin(GL_QUAD_STRIP)
        glColor3f(0.0, 0.2196, 0.5765)
        glVertex2f(0.00, 0.50)
        glVertex2f(-0.05, 0.585)
        glVertex2f(0.75, -0.05)
        glVertex2f(0.825, -0.05)
        glEnd()

        glBegin(GL_QUAD_STRIP)
        glColor3f(0.0, 0.2196, 0.5765)
        glVertex2f(0.75, 0.00)
        glVertex2f(0.75, -0.05)
        glVertex2f(0.248, 0.00)
        glVertex2f(0.30, -0.05)
        glEnd()

        glBegin(GL_QUAD_STRIP)
        glColor3f(0.0, 0.2196, 0.5765)
        glVertex2f(0.75, -0.545)
        glVertex2f(0.810, -0.545)
        glVertex2f(0.30, -0.05)
        glVertex2f(0.357, -0.05)
        glEnd()

        glBegin(GL_QUAD_STRIP)
        glColor3f(0.0, 0.2196, 0.5765)
        glVertex2f(-0.045, -0.50)
        glVertex2f(-0.045, -0.545)
        glVertex2f(0.75, -0.50)
        glVertex2f(0.75, -0.545)
        glEnd()
        glColor3f(0.8275, 0.8275, 0.8275)
        
        # Draw circles on the flag
        draw_circle(0.18, 0.20, 0.1, 100, 2)
        glColor3f(0.8627, 0.0784, 0.2353)
        draw_circle(0.18, 0.24163, 0.09, 100, 2)

        # Draw specific attributes on the flag
        glColor3f(0.8275, 0.8275, 0.8275)
        draw_flag_attributes(0.20, -0.30, 0.065, 12, 2)

        glColor3f(0.8275, 0.8275, 0.8275)
        draw_flag_attributes(0.18, 0.1525, 0.05, 10, 1)
        pygame.display.flip()

# Call the function to draw the Nepal flag
draw_nepal_flag()
