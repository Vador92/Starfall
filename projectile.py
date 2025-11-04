import pygame as pg

class Projectile:
    def __init__(self, position, color, direction, speed, damage, radius):
        self.position = position
        self.color = color
        self.direction = direction.normalize()
        self.speed = speed
        self.damage = damage
        self.radius = radius

    def move(self, last_postion, dt):
        pass