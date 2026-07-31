import pygame
import random
from settings import *


class Obstacle:

    def __init__(self):

        self.image = pygame.image.load(
            "assets/images/enemy.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (ENEMY_WIDTH, ENEMY_HEIGHT)
        )

        self.speed = ENEMY_SPEED

        self.reset()

    def reset(self):

        self.x = random.choice(LANES)
        self.y = -random.randint(300, 900)

        self.rect = pygame.Rect(
            self.x + 12,
            self.y + 12,
            ENEMY_WIDTH - 24,
            ENEMY_HEIGHT - 24
        )

    def update(self):

        self.y += self.speed

        if self.y > HEIGHT:
            self.reset()

        self.rect.x = self.x + 12
        self.rect.y = self.y + 12

    def increase_speed(self):

        self.speed += SPEED_INCREMENT

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))