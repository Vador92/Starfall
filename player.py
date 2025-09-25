import pygame as pg

class Player:
    def __init__(self, position, size):
        self.position : pg.Vector2 = position
        self.size = size
        self.speed = 50
        self.projectile_speed = 1
        self.health = 50
        self.shield = 0
        self.life_steal = 5
        self.life_steal_chance = 0.01
        self.projectile_cooldown = 1
        self.damage_multiplier = 1.00
    
    def draw(self, screen):
        pg.draw.circle(screen, "green", self.position, self.size)
    
    def clamp_player(self, screen):
        self.position.x = max(self.size, min(self.position.x, screen.get_width() - self.size))
        self.position.y = max(self.size, min(self.position.y, screen.get_height() - self.size))

    def get_center(self):
        return self.position.x + self.size / 2, self.position.y + self.size / 2