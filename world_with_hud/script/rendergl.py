import os, sys, ctypes, json
import numpy as np, pygame, glfw
from OpenGL.GL import *

class RenderGL():
    @staticmethod
    def render_cuboid3_color(game, camera, cuboid, color):
        glEnableVertexAttribArray(game.location['a_position'])
        glDisableVertexAttribArray(game.location['a_texcoord'])

        glUniform1i(game.location['u_mode_f'], 1)
        glUniform3f(game.location['u_color'], color[0], color[1], color[2])
        glUniform3f(game.location['u_m_pos'], cuboid.pos.x, cuboid.pos.y, cuboid.pos.z)
        glUniform3f(game.location['u_m_size'], cuboid.size.x, cuboid.size.y, cuboid.size.z)
        glUniform3f(game.location['u_c_pos'], camera.pos.x, camera.pos.y, camera.pos.z)
        glUniform4f(game.location['u_c_proj'], camera.fov, camera.asp, camera.near, camera.far)
        glBindBuffer(GL_ARRAY_BUFFER, game.buffer['cuboid'])
        glVertexAttribPointer(game.location['a_position'], 3, GL_FLOAT, False, 5 * 4, ctypes.c_void_p(0 * 4))
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, game.buffer['cuboid_index'])
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_SHORT, ctypes.c_void_p(0))

    @staticmethod
    def render_cuboid3_texture(game, camera, cuboid, texture):
        glEnableVertexAttribArray(game.location['a_position'])
        glEnableVertexAttribArray(game.location['a_texcoord'])

        glUniform1i(game.location['u_mode_f'], 2)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture['width'], texture['height'], 0, GL_RGBA, GL_UNSIGNED_BYTE, texture['data'])
        glUniform3f(game.location['u_m_pos'], cuboid.pos.x, cuboid.pos.y, cuboid.pos.z)
        glUniform3f(game.location['u_m_size'], cuboid.size.x, cuboid.size.y, cuboid.size.z)
        glUniform3f(game.location['u_c_pos'], camera.pos.x, camera.pos.y, camera.pos.z)
        glUniform4f(game.location['u_c_proj'], camera.fov, camera.asp, camera.near, camera.far)

        glBindBuffer(GL_ARRAY_BUFFER, game.buffer['cuboid'])
        glVertexAttribPointer(game.location['a_position'], 3, GL_FLOAT, False, 5 * 4, ctypes.c_void_p(0 * 4))
        glVertexAttribPointer(game.location['a_texcoord'], 2, GL_FLOAT, False, 5 * 4, ctypes.c_void_p(3 * 4))
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, game.buffer['cuboid_index'])
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_SHORT, ctypes.c_void_p(0))