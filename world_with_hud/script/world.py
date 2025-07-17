from script.asset import *
from script.ui import *

from script.primitive import *
from script.func import *

from script.player import *
from script.rendergl import *
from script.renderhud import *

'''
Handling world and world elements.
'''

# Player in world.
class PlayerWorld():
    pass

# World.
class World():
    def __init__(self):
        self.thing = [
            Cuboid3(0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0),
            Cuboid3(-0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0),
            Cuboid3(-0.2, -0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0),
            Cuboid3(0.2, -0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0),
        ]
        self.camera = Camera3()
        self.light = Vector3(0.0, 0.0, 1.0)

    def handle_tick(self, game):
        self.thing[2].rot.x += 0.5 / game.fps
        self.thing[2].rot.y += 0.5 / game.fps
        self.thing[3].rot.y += 0.5 / game.fps
        self.thing[3].rot.z += 0.5 / game.fps

    def render(self, game):
        RenderGL.render_cuboid3(game, self.camera, self.light, self.thing[0], 1, [0.0, 1.0, 1.0], None)
        RenderGL.render_cuboid3(game, self.camera, self.light, self.thing[1], 2, [0.0, 1.0, 1.0], Texture.test_texture)
        RenderGL.render_cuboid3(game, self.camera, self.light, self.thing[2], 3, [0.0, 1.0, 1.0], None)
        RenderGL.render_cuboid3(game, self.camera, self.light, self.thing[3], 4, [0.0, 1.0, 1.0], Texture.test_texture)
        
# Camera in world.
class Camera3():
    def __init__(self):
        self.pos = Vector3(0, 0, -1.0)
        self.rot = Vector3(0, 0, 0)
        self.near = 0.1
        self.far = 10.0
        self.fov = 60.0 * 3.14 / 180.0
        self.asp = 16.0 / 9.0
