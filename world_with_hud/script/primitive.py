'''
Handling elements in world and shapes.
'''

# 2D vector
class Vector2():
    # Vector2(x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Clone method
    def clone(self):
        return Vector2(self.x, self.y)

# 3D Vector
class Vector3():
    # Vector3(x, y, z)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = z

    # Clone method
    def __clone__(self):
        return Vector3(self.x, self.y, self.z)

# 3D cuboid object
class Cuboid3():
    # Constructor
    def __init__(self, x, y, z, w, h, d):
        self.pos = Vector3(x, y, z)
        self.size = Vector3(w, h, d)
