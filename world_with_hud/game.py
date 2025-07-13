from script.module import *

class Game():
    def __init__(self):
        # Input variable.
        self.mouse_pressed = False
        self.key_binding = {} # Edit this.
        self.key_pressed = {}

        for k in self.key_binding:
            self.key_pressed[k] = False

        self.scene = 'title'
        self.state = ''
        self.menu = False

        self.gl_var = {}

        glfw.init()
        pygame.init()
        pygame.font.init()
        

    def run(self):
        pass

if __name__ == '__main__':
    Game().run()