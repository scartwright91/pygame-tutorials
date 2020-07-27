
import pygame as pg
import sys
from cut_scenes import CutSceneManager, CutSceneOne


pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

# Define player class
class Player(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(400, 300))

    def update(self, cut_scene_manager):

        if self.rect.centerx > 800:
            cut_scene_manager.start_cut_scene(CutSceneOne(self))

        if cut_scene_manager.cut_scene is None:
            pressed = pg.key.get_pressed()
            if pressed[pg.K_LEFT]:
                self.rect.x -= 5
            if pressed[pg.K_RIGHT]:
                self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

# Create player and cut scene manager
player = Player()
cut_scene_manager = CutSceneManager(screen)

# Game loop
while True:

    clock.tick(60)

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Update objects
    player.update(cut_scene_manager)
    cut_scene_manager.update()

    # Draw objects
    screen.fill((255, 255, 255))
    player.draw(screen)
    cut_scene_manager.draw()

    # update display
    pg.display.flip()

