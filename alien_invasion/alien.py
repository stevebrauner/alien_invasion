import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Provides the Alien class for the instantiation of an alien.

    Used by the View class.
    """

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.position_x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False

    def update(self, speed, direction):
        self.position_x += speed * direction
        self.rect.x = self.position_x
