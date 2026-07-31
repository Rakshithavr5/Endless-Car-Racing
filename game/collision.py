import pygame

class Collision:

    @staticmethod
    def check(player, obstacles):

        for obstacle in obstacles:

            if player.rect.colliderect(obstacle.rect):
                return True

        return False