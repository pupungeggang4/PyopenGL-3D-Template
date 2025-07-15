from script.module import *

class RenderGL():
    @staticmethod
    def render_cuboid3_color(game, camera, cuboid, color):
        glUniform1i(game.location['u_mode_f'], 1)
        glUniform3f(game.location['u_color'], color[0], color[1], color[2])
        glBindBuffer(GL_ARRAY_BUFFER, game.buffer['cuboid'])
