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
    
    def clamp_player(self, game_screen):
        self.position.x = max(self.size, min(self.position.x, game_screen.get_width() - self.size))
        self.position.y = max(self.size, min(self.position.y, game_screen.get_height() - self.size))

    def get_center(self):
        return self.position.x + self.size / 2, self.position.y + self.size / 2
    
    def player_update(self, delta):
        if pg.key.get_pressed()[pg.K_LEFT] or pg.key.get_pressed()[pg.K_a]:
            self.position.x -= self.speed * delta
        if pg.key.get_pressed()[pg.K_RIGHT] or pg.key.get_pressed()[pg.K_d]:
            self.position.x += self.speed * delta 
        if pg.key.get_pressed()[pg.K_DOWN] or pg.key.get_pressed()[pg.K_s]:
            self.position.y += self.speed * delta    
        if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_w]:
            self.position.y -= self.speed * delta