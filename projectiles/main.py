
import pygame as pg
import sys
from projectiles import *

pg.init()
screen = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()

projectiles = []
timer = pg.time.get_ticks()

# Game loop
while True:

    clock.tick(60)

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pressed = pg.key.get_pressed()
    mouse_pos = pg.mouse.get_pos()

    if pressed[pg.K_SPACE] and (pg.time.get_ticks() - timer > 500):
        timer = pg.time.get_ticks()
        projectiles.append(
            # add projectile here
            BasicProjectile([0, 500], axis = "x")
        )
        projectiles.append(
            # add projectile here
            LinearProjectile([500, 500], mouse_pos)
        )

    # Update objects
    for p in projectiles:
        p.update()

    # Draw objects
    screen.fill((119, 142, 152))
    for p in projectiles: p.draw(screen)

    # update display
    pg.display.flip()

