import pygame as pg
from player import Player

screen_width, screen_height = 800, 800

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
running = True

screen_rect = screen.get_rect()

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

    player.clamp_player(screen=screen)
    # game rendering done here
    screen.fill("black")
    player.draw(screen=screen)
    pg.display.flip()

pg.quit()