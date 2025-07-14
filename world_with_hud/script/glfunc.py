from script.module import *

class GLFunc():
    @staticmethod
    def gl_init(game):
        width = 1280
        height = 720
        glViewport(0, 0, width, height)