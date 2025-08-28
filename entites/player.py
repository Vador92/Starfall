import pygame as pg

# basic character design and abilities
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
        self.health = 100


    # movement
    def update(self):
        pass

    # shoot towards mouse position
    def shoot(self, mouse_position):
        pass