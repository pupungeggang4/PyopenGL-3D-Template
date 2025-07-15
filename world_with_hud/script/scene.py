import os, sys, ctypes, json
import numpy as np, pygame, glfw
from OpenGL.GL import *

from asset import *
from ui import *
from primitive import *
from func import *
from player import *
from world import *
from rgl import *
from rhud import *
from glfunc import *

def loop(game):
    render(game)

def render(game):
    # Rendering 2D HUD.
    game.surface_hud.fill(Color.transparent)
    pygame.draw.rect(game.surface_hud, Color.white, UI.Scene.test_rect)
    game.surface_hud.blit(Image.test_image, UI.Scene.test_image)
    game.surface_hud.blit(Font.neodgm_32.render('This is UI', False, Color.black), UI.Scene.test_text)

    # Rendering in OpenGL context.
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(game.program)

    # HUD rendering
    glDisable(GL_DEPTH_TEST)
    glUniform1i(game.location['u_mode_v'], 0)
    glUniform1i(game.location['u_mode_f'], 0)
    glEnableVertexAttribArray(game.location['a_position'])
    glEnableVertexAttribArray(game.location['a_texcoord'])
    
    glBindBuffer(GL_ARRAY_BUFFER, game.buffer['hud'])
    glVertexAttribPointer(game.location['a_position'], 2, GL_FLOAT, False, 4 * 4, ctypes.c_void_p(0 * 4))
    glVertexAttribPointer(game.location['a_texcoord'], 2, GL_FLOAT, False, 4 * 4, ctypes.c_void_p(2 * 4))
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, game.buffer['hud_index'])
    surf_texture = pygame.image.tobytes(game.surface_hud, 'RGBA')
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 1280, 720, 0, GL_RGBA, GL_UNSIGNED_BYTE, surf_texture)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, ctypes.c_void_p(0))

    # 3D rendering.
    game.world.render(game)
