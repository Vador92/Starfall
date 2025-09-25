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

    player.player_update(dt)
    

    player.clamp_player(screen)
    # game rendering done here
    screen.fill("black")
    player.draw(screen)
    pg.display.flip()

pg.quit()