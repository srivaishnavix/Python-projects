import pygame as pg 
import numpy as np 

WIDTH = 800
HEIGHT = 8000

black =(0,0,0)
green=(0,255,0)

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(WIDTH,HEIGHT)

class Projection:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width,height))
        self.background = black
        self.surfaces = ()

    def add_surface(self, name, surface):
        self.surfaces[name] = surface
class Object:
    def __init__(self):
        self.nodes = np.zeros((0,4))
    
    def add_nodes(self, node_array):
        ones_column = np.ones((len(node_array),1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes,ones_added))

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()