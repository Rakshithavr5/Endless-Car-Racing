import pygame
from settings import *


class PlayerCar:

    def __init__(self):

        self.image = pygame.image.load(
            "assets/images/player.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        self.x = WIDTH // 2 - PLAYER_WIDTH // 2
        self.y = HEIGHT - PLAYER_HEIGHT - 20

        self.speed = PLAYER_SPEED

        self.rect = pygame.Rect(
            self.x + 12,
            self.y + 12,
            PLAYER_WIDTH - 24,
            PLAYER_HEIGHT - 24
        )

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if self.x < ROAD_LEFT + 10:
            self.x = ROAD_LEFT + 10

        if self.x > ROAD_RIGHT - PLAYER_WIDTH - 10:
            self.x = ROAD_RIGHT - PLAYER_WIDTH - 10

        self.rect.x = self.x + 12
        self.rect.y = self.y + 12

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))