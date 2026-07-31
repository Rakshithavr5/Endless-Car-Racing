import pygame
from settings import *


class Road:

    def __init__(self):

        self.y = 0
        self.speed = ROAD_SPEED

    def update(self):

        self.y += self.speed

        if self.y >= 60:
            self.y = 0

    def draw(self, screen):

        # Sky
        screen.fill((135, 206, 235))

        # Grass
        pygame.draw.rect(screen, (34, 139, 34), (0, 0, ROAD_LEFT, HEIGHT))
        pygame.draw.rect(screen, (34, 139, 34), (ROAD_RIGHT, 0, WIDTH - ROAD_RIGHT, HEIGHT))

        # Grass stripes
        for i in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, (46, 160, 46), (0, i, ROAD_LEFT, 20))
            pygame.draw.rect(screen, (46, 160, 46), (ROAD_RIGHT, i, WIDTH - ROAD_RIGHT, 20))

        # Road shadow
        pygame.draw.rect(screen, (30, 30, 30), (ROAD_LEFT - 6, 0, ROAD_WIDTH + 12, HEIGHT))

        # Road
        pygame.draw.rect(screen, (55, 55, 55), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

        # Yellow side lines
        pygame.draw.line(screen, (255, 215, 0), (ROAD_LEFT + 3, 0), (ROAD_LEFT + 3, HEIGHT), 5)
        pygame.draw.line(screen, (255, 215, 0), (ROAD_RIGHT - 3, 0), (ROAD_RIGHT - 3, HEIGHT), 5)

        # White lane markings
        for y in range(-80, HEIGHT + 80, 80):
            pygame.draw.rect(
                screen,
                WHITE,
                (WIDTH // 2 - 5, y + self.y, 10, 40)
            )