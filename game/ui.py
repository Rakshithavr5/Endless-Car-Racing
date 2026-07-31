import pygame
from settings import *


class UI:

    def __init__(self):
        pass

    def start_screen(self, screen):

        title_font = pygame.font.SysFont("Arial", 64, bold=True)
        text_font = pygame.font.SysFont("Arial", 34)
        small_font = pygame.font.SysFont("Arial", 24)

        while True:

            screen.fill((15, 15, 25))

            title = title_font.render(
                "ENDLESS CAR RACING",
                True,
                (255, 215, 0)
            )

            subtitle = small_font.render(
                "Survive as long as possible!",
                True,
                (200, 200, 200)
            )

            start = text_font.render(
                "Press SPACE to Start",
                True,
                (255, 255, 255)
            )

            controls = small_font.render(
                "Move : Left / Right Arrow Keys",
                True,
                (180, 180, 180)
            )

            pause = small_font.render(
                "P : Pause",
                True,
                (180, 180, 180)
            )

            quit_game = small_font.render(
                "ESC : Quit",
                True,
                (180, 180, 180)
            )

            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 160))
            screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 245))
            screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 320))
            screen.blit(controls, (WIDTH // 2 - controls.get_width() // 2, 390))
            screen.blit(pause, (WIDTH // 2 - pause.get_width() // 2, 430))
            screen.blit(quit_game, (WIDTH // 2 - quit_game.get_width() // 2, 470))

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        return

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

    def pause_screen(self, screen):

        font = pygame.font.SysFont("Arial", 48, bold=True)

        paused = True

        while paused:

            text = font.render("PAUSED", True, (255, 255, 0))

            screen.blit(
                text,
                (WIDTH // 2 - text.get_width() // 2,
                 HEIGHT // 2 - text.get_height() // 2)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_p:
                        paused = False

    def game_over(self, screen, score, high_score, coins):

        title_font = pygame.font.SysFont("Arial", 60, bold=True)
        font = pygame.font.SysFont("Arial", 30)

        while True:

            screen.fill((20, 20, 20))

            title = title_font.render(
                "GAME OVER",
                True,
                (255, 0, 0)
            )

            score_text = font.render(
                f"Score : {score}",
                True,
                WHITE
            )

            high_text = font.render(
                f"High Score : {high_score}",
                True,
                YELLOW
            )

            coin_text = font.render(
                f"Coins Collected : {coins}",
                True,
                (255, 215, 0)
            )

            restart = font.render(
                "Press R to Restart",
                True,
                WHITE
            )

            quit_game = font.render(
                "Press ESC to Exit",
                True,
                WHITE
            )

            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 130))
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 230))
            screen.blit(high_text, (WIDTH // 2 - high_text.get_width() // 2, 280))
            screen.blit(coin_text, (WIDTH // 2 - coin_text.get_width() // 2, 330))
            screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, 410))
            screen.blit(quit_game, (WIDTH // 2 - quit_game.get_width() // 2, 460))

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:
                        return True

                    if event.key == pygame.K_ESCAPE:
                        return False
