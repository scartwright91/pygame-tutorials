
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1000, 600))
TILE_SIZE = 128
clock = pg.time.Clock()

def draw_speech_bubble(screen, text, text_colour, bg_colour, pos, size):

    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, text_colour)
    text_rect = text_surface.get_rect(midbottom=pos)

    # background
    bg_rect = text_rect.copy()
    bg_rect.inflate_ip(10, 10)

    # Frame
    frame_rect = bg_rect.copy()
    frame_rect.inflate_ip(4, 4)

    pg.draw.rect(screen, text_colour, frame_rect)
    pg.draw.rect(screen, bg_colour, bg_rect)
    screen.blit(text_surface, text_rect)


# Read image utility function
def read_image(path, w=None, h=None):

    img = pg.image.load(path)

    if (w == None) and (h == None):
        pass
    elif h == None:
        scale = w / img.get_width()
        h = scale * img.get_height()
        img = pg.transform.scale(img, (int(w), int(h)))
    elif w == None:
        scale = h / img.get_height()
        w = scale * img.get_width()
        img = pg.transform.scale(img, (int(w), int(h)))
    else:
        img = pg.transform.scale(img, (int(w), int(h)))
    
    return img

# Define player class
class Player(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = read_image('gnome.png', w=TILE_SIZE, h=TILE_SIZE)
        self.image = pg.Surface(image.get_size(), pg.SRCALPHA)
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect(topleft=(50, screen.get_height() - TILE_SIZE))

    def update(self):

        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:
            self.rect.x -= 5
        if pressed[pg.K_RIGHT]:
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        draw_speech_bubble(screen, "Hello", (255, 255, 255), (0, 0, 0), self.rect.midtop, 25)

# Define NPC characters
class NPCOne(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image_left = read_image('gnome_npc_one.png', w=TILE_SIZE, h=TILE_SIZE)
        self.image_right = pg.transform.flip(self.image_left, True, False)
        self.image = pg.Surface(self.image_left.get_size(), pg.SRCALPHA)
        self.image.blit(self.image_left, (0, 0))
        self.rect = self.image.get_rect(topleft=(400, screen.get_height() - TILE_SIZE))
        self.speaking = False

    def update(self, player):

        if abs(player.rect.x - self.rect.x) < 100:
            self.speaking = True
        else:
            self.speaking = False

        if player.rect.x < self.rect.x:
            self.image = self.image_left
        else:
            self.image = self.image_right

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        if self.speaking:
            draw_speech_bubble(screen, "Hello Player", (255, 255, 0), (175, 175, 0), self.rect.midtop, 25)


# Create player and NPCs
player = Player()
npc_one = NPCOne()

# Game loop
while True:

    clock.tick(60)

    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Update objects
    player.update()
    npc_one.update(player)

    # Draw objects
    screen.fill((255, 255, 255))
    player.draw(screen)
    npc_one.draw(screen)

    # update display
    pg.display.flip()

