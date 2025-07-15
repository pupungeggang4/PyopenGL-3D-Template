from script.module import *
'''
Handling world and world elements.
'''

# Player in world.
class PlayerWorld():
    pass

# World.
class World():
    def __init__(self):
        self.thing = [Cuboid3(0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0), Cuboid3(-0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0)]
        self.camera = Camera3()

# Camera in world.
class Camera3():
    def __init__(self):
        self.pos = Vector3(0, 0, -1.0)
        self.rot = Vector3(0, 0, 0)
        self.near = 0.1
        self.far = 10.0
        self.fov = 60.0 * 3.14 / 180.0
        self.asp = 16.0 / 9.0
