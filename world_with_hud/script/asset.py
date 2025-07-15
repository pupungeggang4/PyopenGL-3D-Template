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

class Color():
    transparent = [0, 0, 0, 0]
    black = [0, 0, 0]
    white = [255, 255, 255]

class Image():
    pass

class Font():
    pass