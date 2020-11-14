
import pygame as pg
import math



class BasicProjectile:

    def __init__(self, pos, axis = "x"):
        self.pos = pos
        self.axis = axis
        self.speed = 5

    def update(self):
        if self.axis == "x":
            self.pos[0] += self.speed
        elif self.axis == "y":
            self.pos[1] += self.speed

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 0), self.pos, radius = 20)


class LinearProjectile:

    def __init__(self, pos, target_pos):
        self.pos = pos
        self.x_delta = (target_pos[0] - pos[0])
        self.y_delta = -(target_pos[1] - pos[1])
        self.theta = math.atan2(self.y_delta, self.x_delta)
        print(180*self.theta/math.pi)
        self.speed = 5

    def update(self):

        # Distance projectile will travel each update
        h = self.speed

        # Calculate incremental changes x and y
        x_increment = h * math.sin(self.theta)
        y_increment = h * math.cos(self.theta)

        # update projectile's position
        self.pos[0] += x_increment
        self.pos[1] += y_increment

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 0), self.pos, radius = 20)




