import pygame
from pygame.math import Vector2

class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.speed = 1.3
        self.gravity = 0.5

        size = self.game.screen.get_size()

        self.pos = Vector2(size[0]/2,size[1]/2)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)

    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))

        # Physics
        self.vel *= 0.8 # opór powietrza
        self.vel -= Vector2(0, -self.gravity) # grawitacja

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0


    def draw(self):
        # Base triangle
        points = [Vector2(0,-10), Vector2(5,5), Vector2(-5,5)]

        # Rotate points
        angle = self.vel.angle_to(Vector2(0,1)) # kąt między linią poziomą a prędkością
        points = [p.rotate(angle) for p in points]

        # Fix y axis
        points = [Vector2(p.x, p.y*-1) for p in points]

        # Add current position
        points = [self.pos+p*2 for p in points]

        pygame.draw.polygon(self.game.screen, (0,100,255),points)

