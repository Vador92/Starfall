import pygame as pg

screen_width, screen_height = 800, 800

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
running = True

screen_rect = screen.get_rect()

class Player:
    def __init__(self, position, size):
        self.position : pg.Vector2 = position
        self.size = size
        self.speed = 50
        self.projectile-speed = 1
        self.health = 50
        self.shield = 0
        self.life-steal = 5
        self.life-steal-chance = 0.01
        self.projectile-cooldown = 1
        self.damage-multiplier = 1.00
    
    def draw(self):
        pg.draw.circle(screen, "green", self.position, self.size)
    
    def clamp_player(self):
        self.position.x = max(self.size, min(self.position.x, screen.get_width() - self.size))
        self.position.y = max(self.size, min(self.position.y, screen.get_height() - self.size))

    def get_center(self):
        return self.position.x + self.size / 2, self.position.y + self.size / 2

player = Player(pg.Vector2(50,50), 20)

while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if pg.key.get_pressed()[pg.K_LEFT] or pg.key.get_pressed()[pg.K_a]:
        player.position.x -= player.speed * dt
    if pg.key.get_pressed()[pg.K_RIGHT] or pg.key.get_pressed()[pg.K_d]:
        player.position.x += player.speed * dt 
    if pg.key.get_pressed()[pg.K_DOWN] or pg.key.get_pressed()[pg.K_s]:
        player.position.y += player.speed * dt    
    if pg.key.get_pressed()[pg.K_UP] or pg.key.get_pressed()[pg.K_w]:
        player.position.y -= player.speed * dt

    player.clamp_player()
    # game rendering done here
    screen.fill("black")
    player.draw()
    pg.display.flip()

pg.quit()