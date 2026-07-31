import pygame
import random
from settings import *


class Coin:

    def __init__(self):

        self.radius = 12

        self.x = random.choice(LANES)

        self.y = random.randint(-800, -200)

        self.speed = ENEMY_SPEED

        self.value = 20

        self.rect = pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def update(self):

        self.y += self.speed

        if self.y > HEIGHT + 20:

            self.respawn()

        self.rect.center = (self.x, self.y)

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 215, 0),
            (self.x, self.y),
            self.radius
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (self.x, self.y),
            self.radius,
            2
        )

    def respawn(self):

        self.x = random.choice(LANES)

        self.y = random.randint(-900, -300)
