import pygame
import os
from settings import *


class Score:

    def __init__(self):

        self.score = 0
        self.distance = 0
        self.coins = 0
        self.high_score = 0

        self.font = pygame.font.SysFont("Arial", FONT_SIZE, bold=True)

        self.load_high_score()

    def update(self, road_speed):

        self.score += 1
        self.distance += road_speed

    def increase_difficulty(self, road, obstacles):

        # Increase speed every LEVEL_UP_SCORE
        if self.score != 0 and self.score % LEVEL_UP_SCORE == 0:

            road.speed += SPEED_INCREMENT

            for obstacle in obstacles:
                obstacle.increase_speed()

    def game_over(self):

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def reset(self):

        self.score = 0
        self.distance = 0
        self.coins = 0

    def draw(self, screen, speed):

        panel = pygame.Surface((240, 230))
        panel.set_alpha(170)
        panel.fill((20, 20, 20))
        screen.blit(panel, (15, 15))

        score = self.font.render(
            f"Score : {self.score}",
            True,
            (255, 255, 255)
        )

        distance = self.font.render(
            f"Distance : {self.distance}",
            True,
            (255, 255, 255)
        )

        speed_text = self.font.render(
            f"Speed : {speed}",
            True,
            (255, 255, 255)
        )

        high = self.font.render(
            f"High Score : {self.high_score}",
            True,
            (255, 215, 0)
        )

        coins = self.font.render(
            f"Coins : {self.coins}",
            True,
            (255, 255, 0)
        )

        screen.blit(score, (30, 30))
        screen.blit(distance, (30, 70))
        screen.blit(speed_text, (30, 110))
        screen.blit(high, (30, 150))
        screen.blit(coins, (30, 190))

    def load_high_score(self):

        if os.path.exists("highscore.txt"):

            with open("highscore.txt", "r") as file:

                try:
                    self.high_score = int(file.read())
                except:
                    self.high_score = 0

    def save_high_score(self):

        with open("highscore.txt", "w") as file:

            file.write(str(self.high_score))