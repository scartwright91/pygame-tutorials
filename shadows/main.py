import pygame as pg
import sys
import math

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1200, 800))

# Read images
tree = pg.image.load("tree.png").convert_alpha()
tree = pg.transform.scale(tree, (192, 360))
king = pg.image.load("king.png").convert_alpha()
king = pg.transform.scale(king, (78, 116))
grass = pg.image.load("grass.png").convert()
grass = pg.transform.scale(grass, (1200, 300))
sky = pg.image.load("sky_gradient.png").convert()
sky = pg.transform.scale(sky, (1200, 800))

king_mask = pg.mask.from_surface(king).outline()
king_mask = [(x + 600, y + 386) for x, y in king_mask]

sun_pos = pg.Vector2(0, 0)
target_pos = pg.Vector2(600, 400)
sun_angle = math.atan2((sun_pos.x - target_pos.x), (sun_pos.y - target_pos.y))

shadows = []

for x, y in king_mask:

    shadow_height = (500 - y) * 1.3
    shadow_width = shadow_height * math.tan(sun_angle)
    shadow_point = (x + shadow_width, y + shadow_height)
    shadows.append(shadow_point)

while True:

    clock.tick(60)

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Draw screen
    screen.fill((0, 0, 0))
    screen.blit(sky, (0, 0))
    screen.blit(grass, (0, 500))
    screen.blit(king, (600, 386))
    screen.blit(tree, (250, 140))

    pg.draw.polygon(screen, (0, 0, 0), shadows)

    pg.display.flip()



