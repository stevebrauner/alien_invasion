import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ship_top, color, width, height):
        super().__init__()
        self.screen = screen

        self.color = color

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.midtop = ship_top

        self.position_y = float(self.rect.y)

    def update(self, speed):
        self.position_y -= speed
        self.rect.y = self.position_y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
