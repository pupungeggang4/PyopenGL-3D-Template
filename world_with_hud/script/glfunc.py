from script.module import *

class GLFunc():
    @staticmethod
    def gl_init(game):
        game.shader_v = glCreateShader(GL_VERTEX_SHADER)
        game.program = glCreateProgram()