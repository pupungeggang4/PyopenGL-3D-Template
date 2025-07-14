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

        # Initializing GLFW
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        glfw.window_hint(glfw.SCALE_TO_MONITOR, True)
        self.window = glfw.create_window(1280, 720, 'buffer test', None, None)
        self.context = glfw.make_context_current(self.window)
        self.monitor = glfw.get_primary_monitor()
        self.video_mode = glfw.get_video_mode(self.monitor)
        self.scale = glfw.get_window_content_scale(self.window)

        glfw.set_window_pos(self.window, int(self.video_mode.size.width / 2 - 1280 * self.scale[0] / 2), int(self.video_mode.size.height / 2.0 - 720 * self.scale[1] / 2))
        glfw.set_window_close_callback(self.window, self.cb_window_close)
        glfw.set_mouse_button_callback(self.window, self.cb_mouse_button)
        glfw.set_key_callback(self.window, self.cb_key)

        GLFunc.gl_init(self.gl_var)
        self.pg_init()

    # A function which initializes Pygame
    # Pygame is used in making 2d hud, handling audio, and clock
    def pg_init(self):
        pygame.init()
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
        Font.neodgm_16 = pygame.font.Font('font/neodgm.ttf', 16)
        Image.test_image = pygame.image.load('image/test_image.png')

        self.surface = pygame.surface.Surface([1280, 720], pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while not glfw.window_should_close(self.window):
            self.clock.tick(self.fps)
            glfw.swap_buffers(self.window)
            glfw.poll_events()

    def cb_window_close(self, window):
        glfw.set_window_should_close(window, True)

    def cb_key(self, window, key, scancode, action, mods):
        pass

    def cb_mouse_button(self, window, button, action, mods):
        pos = list(glfw.get_cursor_pos(self.window))

        if sys.platform != 'darwin':
            pos[0] /= 2
            pos[1] /= 2

        print(pos)

if __name__ == '__main__':
    Game().run()