import glfw

def main():
    if not glfw.init():
        return

    monitor = glfw.get_primary_monitor()
    mode = glfw.get_video_mode(monitor)
    width, height = mode.size.width, mode.size.height
    print("Screen resolution: {}x{}".format(width, height))

    glfw.terminate()

if __name__ == "__main__":
    main()