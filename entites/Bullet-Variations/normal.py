import pygame as pg
from bullet import Bullet

class Normal(Bullet):
    def __init__(self, x, y):
        Bullet.__init__(self, x, y)

        self.damage = 20