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
        GLFunc.gl_init(self.gl_var)
        self.pg_init()

    def pg_init(self):
        pygame.init()
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
        Font.neodgm_16 = pygame.font.Font('font/neodgm.ttf', 16)

        self.surface = pygame.surface.Surface([1280, 720], pygame.SRCALPHA)

    def run(self):
        pass

if __name__ == '__main__':
    Game().run()