import os, sys, ctypes, json
import numpy as np, pygame, glfw
from OpenGL.GL import *

from script.asset import *
from script.ui import *
from script.primitive import *
from script.func import *
from script.save import *
from script.player import *
from script.world import *
from script.rendergl import *
from script.renderhud import *
from script.glfunc import *

import script.scene as scene

class Game():
    def __init__(self):
        # Loading save data.
        self.save_data = {}
        read_save_data(self)
        print(self.save_data)

        # Input variable.
        self.mouse_pressed = False
        self.key_binding = {} # Edit this.
        self.key_pressed = {}

        for k in self.key_binding:
            self.key_pressed[k] = False

        # World
        self.world = World()

        # Scene and state variable
        self.scene = 'scene'
        self.state = ''
        self.menu = False

        # Initializing GLFW
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
        glfw.window_hint(glfw.SCALE_TO_MONITOR, True)
        glfw.window_hint(glfw.RESIZABLE, False)
        self.window = glfw.create_window(1280, 720, 'world with hud template', None, None)
        self.context = glfw.make_context_current(self.window)
        self.monitor = glfw.get_primary_monitor()
        self.video_mode = glfw.get_video_mode(self.monitor)
        self.scale = glfw.get_window_content_scale(self.window)

        if sys.platform != 'darwin':
            glfw.set_window_pos(self.window, int(self.video_mode.size.width / 2 - 1280 * self.scale[0] / 2), int(self.video_mode.size.height / 2.0 - 720 * self.scale[1] / 2))

        glfw.set_window_close_callback(self.window, self.cb_window_close)
        glfw.set_mouse_button_callback(self.window, self.cb_mouse_button)
        glfw.set_key_callback(self.window, self.cb_key)

        # Initializing OpenGL (Defined in script/glfunc.py)
        GLFunc.gl_init(self)

        # Initializing pygame (Defined below.)
        self.pg_init()

    # A function which initializes Pygame
    # Pygame is used in making 2d hud, handling audio, and clock
    def pg_init(self):
        pygame.init()
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
        Font.neodgm_16 = pygame.font.Font('font/neodgm.ttf', 16)
        Image.test_image = pygame.image.load('image/test_image.png')
        Texture.test_texture = {
            'width': 40, 'height': 40, 'data': pygame.image.tobytes(pygame.image.load('image/test_image.png'), 'RGBA')
        }

        self.surface_hud = pygame.surface.Surface([1280, 720], pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while not glfw.window_should_close(self.window):
            self.clock.tick(self.fps)
            if self.scene == 'scene':
                scene.loop(self)
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