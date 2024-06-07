import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# The cube's vertices
cube_vertices = [
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Bottom face
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]  # Top face
]

# The cube's edges using vertex indices
cube_edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # Bottom face edges
    [4, 5], [5, 6], [6, 7], [7, 4],  # Top face edges
    [0, 4], [1, 5], [2, 6], [3, 7]  # Vertical edges connecting top and bottom faces
]

def draw_cube(vertices):
    glBegin(GL_LINES)
    for edge in cube_edges:
        for vertex_index in edge:
            glVertex3fv(vertices[vertex_index])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)  # Initial camera position
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Original Cube
        glColor3f(0.0, 1.0, 0.0)  # Green color
        draw_cube(cube_vertices)

        # Rotated Cube
        glPushMatrix()
        glRotatef(5, 5, 5, 5)  # Rotate by 5 degrees on all axes
        glColor3f(1.0, 0.0, 0.0)  # Red color
        draw_cube(cube_vertices)
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
