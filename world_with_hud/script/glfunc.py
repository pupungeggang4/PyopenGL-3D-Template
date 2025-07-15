from script.module import *

class GLFunc():
    @staticmethod
    def gl_init(game):
        f = open('shader/vertex.vert')
        source_v = f.read().strip('\n')
        f.close()
        f = open('shader/fragment.frag')
        source_f = f.read().strip('\n')
        f.close()
        game.shader_v = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(game.shader_v, source_v)
        glCompileShader(game.shader_v)
        game.shader_f = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(game.shader_f, source_f)
        glCompileShader(game.shader_f)
        game.program = glCreateProgram()
        glAttachShader(game.program, game.shader_v)
        glAttachShader(game.program, game.shader_f)
        glLinkProgram(game.program)

        if not glGetShaderiv(game.shader_v, GL_COMPILE_STATUS):
            print('v', glGetShaderInfoLog(game.shader_v))
        if not glGetShaderiv(game.shader_f, GL_COMPILE_STATUS):
            print('f', glGetShaderInfoLog(game.shader_f))

        # Setting locations.
        game.location = {}
        game.location['a_position'] = glGetAttribLocation(game.program, 'a_position')
        game.location['a_texcoord'] = glGetAttribLocation(game.program, 'a_texcoord')
        game.location['u_mode_v'] = glGetUniformLocation(game.program, 'u_mode_v')
        game.location['u_mode_f'] = glGetUniformLocation(game.program, 'u_mode_f')
        game.location['u_m_pos'] = glGetUniformLocation(game.program, 'u_m_pos')
        game.location['u_m_size'] = glGetUniformLocation(game.program, 'u_m_size')
        game.location['u_m_rot'] = glGetUniformLocation(game.program, 'u_m_rot')
        game.location['u_c_proj'] = glGetUniformLocation(game.program, 'u_c_proj')
        game.location['u_c_pos'] = glGetUniformLocation(game.program, 'u_c_pos')
        game.location['u_c_rot'] = glGetUniformLocation(game.program, 'u_c_rot')
        game.location['u_color'] = glGetUniformLocation(game.program, 'u_color')

        # Vaos and buffers.
        game.vao = 1
        glGenVertexArrays(game.vao)
        glBindVertexArray(game.vao)
        game.buffer = {
            'triangle': 1, 'triangle_index': 2, 'hud': 3, 'hud_index': 4, 'cuboid': 5, 'cuboid': 6
        }
        glGenBuffers(1, game.buffer['triangle'])
        glGenBuffers(1, game.buffer['triangle_index'])

        glBindBuffer(GL_ARRAY_BUFFER, game.buffer['triangle'])
        glBufferData(GL_ARRAY_BUFFER, np.array([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0], dtype = np.float32), GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, game.buffer['triangle_index'])
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, np.array([0, 1, 2], dtype = np.int16), GL_STATIC_DRAW)

        # Textures
        game.texture = 1
        glGenTextures(1, game.texture)
        glBindTexture(GL_TEXTURE_2D, game.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)