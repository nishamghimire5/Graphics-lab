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