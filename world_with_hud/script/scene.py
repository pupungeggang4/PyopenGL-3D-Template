from script.module import *

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
    glUniform1i(game.location['u_mode_v'], 0)

    # 3D rendering.
    glUniform1i(game.location['u_mode_v'], 1)
    glUniform1i(game.location['u_mode_f'], 1)
    glUniform3f(game.location['u_color'], 0.0, 0.0, 1.0)

    glEnableVertexAttribArray(game.location['a_position'])

    glBindVertexArray(game.vao)
    glBindBuffer(GL_ARRAY_BUFFER, game.buffer['triangle'])
    glVertexAttribPointer(game.location['a_position'], 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, game.buffer['triangle_index'])
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_SHORT, ctypes.c_void_p(0))
