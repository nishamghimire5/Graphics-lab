import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# Constants defining the region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

def lineDDA(x0, y0, xEnd, yEnd):
    dx = xEnd - x0
    dy = yEnd - y0
    x = x0
    y = y0

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xIncrement = float(dx) / float(steps)
    yIncrement = float(dy) / float(steps)

    glBegin(GL_POINTS)

    for _ in range(int(steps) + 1):
        glVertex2d(round(x), round(y))
        x += xIncrement
        y += yIncrement

    glEnd()

def calculate_intersection(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denominator = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))

    # Check if the lines are parallel or coincident
    if denominator == 0:
        return None

    px = (((x1 * y2) - (y1 * x2)) * (x3 - x4) - (x1 - x2) * ((x3 * y4) - (y3 * x4))) / denominator
    py = (((x1 * y2) - (y1 * x2)) * (y3 - y4) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) / denominator

    return px, py

def sutherland_hodgman(subject_polygon, clip_polygon):
    output_list = subject_polygon[:]
    clip_edges = len(clip_polygon)
    result = []

    for i in range(clip_edges):
        input_list = output_list[:]
        output_list.clear()

        edge_start = clip_polygon[i]
        edge_end = clip_polygon[(i + 1) % clip_edges]

        for j in range(len(input_list)):
            current_point = input_list[j]
            previous_point = input_list[(j - 1) % len(input_list)]

            # Check if the current point is inside or outside the clipping edge
            if (edge_end[0] - edge_start[0]) * (current_point[1] - edge_start[1]) - (edge_end[1] - edge_start[1]) * (
                    current_point[0] - edge_start[0]) >= 0:
                if (edge_end[0] - edge_start[0]) * (previous_point[1] - edge_start[1]) - (
                        edge_end[1] - edge_start[1]) * (previous_point[0] - edge_start[0]) < 0:
                    # Calculate intersection point and add it to the output list
                    intersection = calculate_intersection(edge_start, edge_end, previous_point, current_point)
                    if intersection:
                        output_list.append(intersection)
                output_list.append(current_point)
            elif (edge_end[0] - edge_start[0]) * (previous_point[1] - edge_start[1]) - (
                    edge_end[1] - edge_start[1]) * (previous_point[0] - edge_start[0]) >= 0:
                # Calculate intersection point and add it to the output list
                intersection = calculate_intersection(edge_start, edge_end, previous_point, current_point)
                if intersection:
                    output_list.append(intersection)

    result = output_list

    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-SCREEN_WIDTH / 2, SCREEN_WIDTH / 2, -SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Draw the original subject polygon
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_LINE_LOOP)
        for vertex in subject_polygon:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

        # Draw the clipping window
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINE_LOOP)
        for vertex in clip_polygon:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

        # Draw the resulting clipped polygon
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINE_LOOP)
        for vertex in result:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

        pygame.display.flip()

subject_polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 300), (200, 250), (150, 350), (100, 350), (100, 200)]
clip_polygon = [(100, 100), (300, 100), (300, 300), (100, 300)]

sutherland_hodgman(subject_polygon, clip_polygon)
