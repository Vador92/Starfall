import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 400))
clock = pg.time.Clock()
running = True

active_bullets = []

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")

    # game rendering done here
    active_bullets.append()


    pg.display.flip()
    

    clock.tick(60)

pg.quit()