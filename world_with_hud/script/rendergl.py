import os, sys, ctypes, json
import numpy as np, pygame, glfw
from OpenGL.GL import *

'''
Functions related to OpenGL rendering objects.
'''

# RenderGL
# Mode 1: no light color, 2: no light texture, 3: light color, 4: light texture 
class RenderGL():
    @staticmethod
    def render_cuboid3(game, camera, light, cuboid, mode, color, texture):
        glUniform1i(game.location['u_mode_f'], mode)

        if mode == 1 or mode == 3:
            glUniform3f(game.location['u_color'], color[0], color[1], color[2])
        elif mode == 2 or mode == 4:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture['width'], texture['height'], 0, GL_RGBA, GL_UNSIGNED_BYTE, texture['data'])
            
        glUniform3f(game.location['u_m_pos'], cuboid.pos.x, cuboid.pos.y, cuboid.pos.z)
        glUniform3f(game.location['u_m_size'], cuboid.size.x, cuboid.size.y, cuboid.size.z)
        glUniform3f(game.location['u_m_rot'], cuboid.rot.x, cuboid.rot.y, cuboid.rot.z)
        glUniform3f(game.location['u_c_pos'], camera.pos.x, camera.pos.y, camera.pos.z)
        glUniform4f(game.location['u_c_proj'], camera.fov, camera.asp, camera.near, camera.far)
        glUniform3f(game.location['u_light_d'], light.x, light.y, light.z)

        glBindBuffer(GL_ARRAY_BUFFER, game.buffer['cuboid'])
        glVertexAttribPointer(game.location['a_position'], 3, GL_FLOAT, False, 8 * 4, ctypes.c_void_p(0 * 4))
        glVertexAttribPointer(game.location['a_texcoord'], 2, GL_FLOAT, False, 8 * 4, ctypes.c_void_p(3 * 4))
        glVertexAttribPointer(game.location['a_normal'], 3, GL_FLOAT, False, 8 * 4, ctypes.c_void_p(5 * 4))
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, game.buffer['cuboid_index'])

        glEnableVertexAttribArray(game.location['a_position'])
        glEnableVertexAttribArray(game.location['a_texcoord'])
        glEnableVertexAttribArray(game.location['a_normal'])
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_SHORT, ctypes.c_void_p(0))