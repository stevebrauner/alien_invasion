import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    The Ship class instantiates a ship.

    It's used by the View and Scoreboard classes.
    """

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.position_x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self, speed):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.position_x += speed
        if self.moving_left and self.rect.left > 0:
            self.position_x -= speed

        self.rect.x = self.position_x

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.position_x = float(self.rect.x)
