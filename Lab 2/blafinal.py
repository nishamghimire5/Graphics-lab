import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader
import numpy as np

width = 500
height = 500


def coordinateChange(previous):
    new = []
    for i in range(len(previous)):
        if ((i+1) % 3 == (1 or 2)):
            new.append(previous[i] / width)
        else:
            new.append(previous[i])
    return new


def BLA(start, end):

    plotted_points = []

    dx = end[0] - start[0]
    dy = end[1] - start[1]

    m = abs(dy / dx)
    x = [
        start[0], start[1], start[2]
    ]

    if (m < 1):
        p_init = 2 * dy - dx
        for i in range(dx):
            if (p_init < 0):
                x = [ x[0] + 1, x[1], x[2]]
                p_next = p_init + 2 * dy
            else:
                x = [ x[0] + 1, x[1] + 1, x[2]]
                p_next = p_init + 2 * dy - 2 * dx
            p_init = p_next
            plotted_points.extend([x[0], x[1], x[2]])
    else:
        p_init = 2 * dx - dy
        for j in range(dy):
            if (p_init < 0):
                x = [ x[0], x[1] + 1, x[2]]
                p_next = p_init + 2 * dx
            else:
                x = [ x[0] + 1, x[1] + 1, x[2]]
                p_next = p_init + 2 * dx - 2 * dy
            p_init = p_next
            plotted_points.extend([x[0], x[1], x[2]])
    return plotted_points


def DDA(start, end):

    plotted_points = []
    
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    x = [start[0], start[1], start[2]]

    if (abs(dx) > abs(dy)):
        step_size = dx
    else:
        step_size = dy

    x_inc = dx / step_size
    y_inc = dy / step_size

    for i in range(step_size):
        x = [x[0] + x_inc, x[1] + y_inc, 0]
        plotted_points.extend([x[0], x[1], x[2]])
    
    return plotted_points


def draw_line_graph(mode, points):

    output_points = []

    if (mode == "BLA"):

        for i in range(len(points)-1):
            start = [points[i][0], points[i][1], points[i][2]]
            end = [points[i+1][0], points[i+1][1], points[i+1][2]]
            output_points.extend(BLA(start, end))

    elif (mode == "DDA"):

        for i in range(len(points)-1):
            start = [points[i][0], points[i][1], points[i][2]]
            end = [points[i+1][0], points[i+1][1], points[i+1][2]]
            output_points.extend(DDA(start, end))

    else:
        print("Wrong Mode!")
    
    return(output_points)


points = [
    [-350,-400, 0],
    [-250,-350, 0],
    [-200,-100, 0],
    [-100,-100, 0],
    [   0, 100, 0],
    [ 150, 200, 0],
    [ 200, 350, 0]
]

input_points = draw_line_graph("BLA", points)
points = coordinateChange(input_points)
points = np.array(points, dtype=np.float32)


def main():
    
    if not glfw.init():
        return
    
    window = glfw.create_window(width, height, "Line", None, None)

    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, points.nbytes, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    vertex_shader = """
    #version 330 core
    layout (location = 0) in vec3 aPos;

    void main()
    {
        gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
    }
    """

    fragment_shader = """
    #version 330 core
    uniform vec4 lineColor;  // Uniform color variable
    out vec4 FragColorOut;

    void main()
    {
        FragColorOut = lineColor;
    }
    """

    shader_program = glCreateProgram()
    vertex_shader_compiled = compileShader(vertex_shader, GL_VERTEX_SHADER)
    fragment_shader_compiled = compileShader(fragment_shader, GL_FRAGMENT_SHADER)

    glAttachShader(shader_program, vertex_shader_compiled)
    glAttachShader(shader_program, fragment_shader_compiled)
    glLinkProgram(shader_program)

    glUseProgram(shader_program)
    
    glfw.make_context_current(window)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUniform4f(glGetUniformLocation(shader_program, "lineColor"), 1.0, 0.22, 0.58, 1.0)
        glDrawArrays(GL_POINTS, 0, 1000)

        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
