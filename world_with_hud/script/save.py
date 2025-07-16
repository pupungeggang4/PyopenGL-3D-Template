import os, sys, ctypes, json
import numpy as np, pygame, glfw
from OpenGL.GL import *

'''
Function related to saving and loading game.
'''

empty_save = {'data': []} # Edit this

def read_save_data(game):
    try:
        f = open('save/save.txt', 'r')
        game.save_data = json.loads(f.read())
        f.close()

    except:
        f = open('save/save.txt', 'w')
        f.write(json.dumps(empty_save))
        f.close()
        f = open('save/save.txt', 'r')
        game.save_data = json.loads(f.read())
        f.close()

def write_save_data(save_data):
    f = open('save/save.txt', 'w')
    f.write(json.dumps(save_data))
    f.close()