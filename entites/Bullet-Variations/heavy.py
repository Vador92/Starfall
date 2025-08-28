import pygame as pg
from bullet import Bullet

class Heavy(Bullet):
    def __init__(self, x, y):
        Bullet.__init__(self, x, y)

        self.damage = 50