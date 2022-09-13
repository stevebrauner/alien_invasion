import pygame.font


class Button:
    """
    The Button class instantiates a button.

    It's used in the View class.
    """

    def __init__(self, screen, message):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.background_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(message)

    def _prep_message(self, message):
        self.message_image = self.font.render(
            message, True, self.text_color, self.background_color
        )
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
