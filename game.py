import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
running = True

class Player:
    def __init__(self, position, size):
        self.position : pg.Vector2 = position
        self.size = size
        self.speed = 200
    
    def draw(self):
        pg.draw.circle(screen, "green", self.position, self.size).clamp_ip(screen.get_rect())


player = Player(pg.Vector2(300,300), 20)

while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if pg.key.get_pressed()[pg.K_LEFT]:
        player.position.x -= player.speed * dt
    if pg.key.get_pressed()[pg.K_RIGHT]:
        player.position.x += player.speed * dt 
    if pg.key.get_pressed()[pg.K_DOWN]:
        player.position.y += player.speed * dt    
    if pg.key.get_pressed()[pg.K_UP]:
        player.position.y -= player.speed * dt

    # game rendering done here
    screen.fill("black")
    player.draw()
    pg.display.flip()

pg.quit()