import pygame

from settings import *
from game.car import PlayerCar
from game.road import Road
from game.obstacle import Obstacle
from game.collision import Collision
from game.score import Score
from game.ui import UI
from game.coin import Coin


class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Endless Car Racing")

        # Audio
        pygame.mixer.init()

        pygame.mixer.music.load("assets/sounds/background.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.crash_sound = pygame.mixer.Sound("assets/sounds/crash.wav")
        self.crash_sound.set_volume(1.0)

        self.clock = pygame.time.Clock()

        self.road = Road()
        self.player = PlayerCar()

        # Start with ONE enemy only
        self.obstacles = [
            Obstacle()
        ]

        self.obstacles[0].y = -500

        self.score = Score()
        self.ui = UI()

        # Coin
        self.coin = Coin()

    def reset(self):

        self.player = PlayerCar()

        # Reset with ONE enemy
        self.obstacles = [
            Obstacle()
        ]

        self.obstacles[0].y = -500

        self.road = Road()

        self.score.reset()

        # Reset Coin
        self.coin.respawn()

    def run(self):

        self.ui.start_screen(self.screen)

        running = True

        while running:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    elif event.key == pygame.K_p:
                        self.ui.pause_screen(self.screen)

            # Move Player
            self.player.move()

            # Update Road
            self.road.update()

            # Update Obstacles
            for obstacle in self.obstacles:
                obstacle.update()

            # Keep Coin speed in sync with the road
            self.coin.speed = self.road.speed

            # Update Coin
            self.coin.update()

            # Coin Collision
            if self.player.rect.colliderect(self.coin.rect):

                self.score.score += self.coin.value
                self.score.coins += 1

                self.coin.respawn()

            # Update Score
            self.score.update(self.road.speed)

            # Increase Speed
            self.score.increase_difficulty(
                self.road,
                self.obstacles
            )

            # Add second enemy
            if self.score.score >= 300 and len(self.obstacles) == 1:

                enemy = Obstacle()
                enemy.y = -700
                self.obstacles.append(enemy)

            # Add third enemy
            if self.score.score >= 700 and len(self.obstacles) == 2:

                enemy = Obstacle()
                enemy.y = -1200
                self.obstacles.append(enemy)

            # Collision
            if Collision.check(
                self.player,
                self.obstacles
            ):

                self.crash_sound.play()

                pygame.mixer.music.stop()

                pygame.time.delay(1000)

                self.score.game_over()

                restart = self.ui.game_over(
                    self.screen,
                    self.score.score,
                    self.score.high_score,
                    self.score.coins
                )

                if restart:

                    self.reset()

                    pygame.mixer.music.play(-1)

                    continue

                else:

                    break

            # Draw
            self.road.draw(self.screen)

            self.coin.draw(self.screen)

            for obstacle in self.obstacles:
                obstacle.draw(self.screen)

            self.player.draw(self.screen)

            self.score.draw(
                self.screen,
                self.obstacles[0].speed
            )

            pygame.display.flip()
