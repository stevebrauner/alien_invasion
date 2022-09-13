import pygame
from alien import Alien
from bullet import Bullet
from button import Button
from scoreboard import Scoreboard
from settings import ViewSettings
from ship import Ship


class View:
    """
    The View class for the Alien Invasion game.

    Its settings are located in the ViewSettings class.
    It uses the Bullet, Alien, Button, and Scoreboard classes to create
    the elements of the view.
    """

    def __init__(self):
        self.settings = ViewSettings()

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion!")

        self.scoreboard = Scoreboard(self.screen)

        self.ship = Ship(self.screen)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self.create_fleet()

        self.play_button = Button(self.screen, "Play")

    def prep_score(self, score):
        self.scoreboard.prep_score(score, self._get_background_color())

    def prep_high_score(self, high_score):
        self.scoreboard.prep_high_score(high_score, self._get_background_color())

    def prep_level(self, level):
        self.scoreboard.prep_level(level, self._get_background_color())

    def _get_background_color(self):
        return self.settings.background_color

    def prep_ships_left(self, ships_left):
        self.scoreboard.prep_ships(ships_left)

    def draw_scoreboard(self):
        self.scoreboard.draw()

    def was_button_clicked(self, mouse_position):
        return self.play_button.rect.collidepoint(mouse_position)

    def get_ship_speed(self):
        return self.settings.ship_speed

    def set_ship_moving_right(self, flag):
        self.ship.moving_right = flag

    def set_ship_moving_left(self, flag):
        self.ship.moving_left = flag

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(
                self.screen,
                self.ship.rect.midtop,
                self.settings.bullet_color,
                self.settings.bullet_width,
                self.settings.bullet_height,
            )
            self.bullets.add(new_bullet)

    def update_ship(self, ship_speed):
        self.ship.update(ship_speed)

    def clear_bullets(self):
        self.bullets.empty()

    def update_bullets(self):
        self.bullets.update(self.settings.bullet_speed)

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def check_and_get_bullet_alien_hits(self):
        hits = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True,
            True,
        )
        return hits

    def get_aliens(self):
        return self.aliens

    def update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update(self.settings.alien_speed, self.settings.fleet_direction)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def is_ship_hit(self):
        if pygame.sprite.spritecollideany(
            self.ship,
            self.aliens,
        ):
            self._ship_hit()
            return True
        return False

    def _ship_hit(self):
        self.aliens.empty()
        self.bullets.empty()
        self.create_fleet()
        self.ship.center_ship()

    def has_alien_hit_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat as if ship got hit.
                self._ship_hit()
                return True
        return False

    def do_aliens_exist(self):
        if not self.aliens:
            return True
        return False

    def update_scoreboard(self):
        self.scoreboard.prep_score()
        self.scoreboard.check_high_score()

    def update_view_level(self):
        self.bullets.empty()
        self.create_fleet()
        self.scoreboard.prep_level()

    def update_screen(self, isGameActive):
        self.screen.fill(self.settings.background_color)
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)

        self.scoreboard.draw()

        if not isGameActive:
            self.play_button.draw()

        pygame.display.flip()

    def reset_view(self):
        self.aliens.empty()
        self.bullets.empty()
        self.create_fleet()
        self.ship.center_ship()

    def create_fleet(self):
        alien = Alien(self.screen)
        alien_width, alien_height = alien.rect.size
        available_row_space = self.settings.screen_width - (2 * alien_width)
        aliens_per_row = available_row_space // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_column_space = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        aliens_per_column = available_column_space // (2 * alien_height)

        for row_number in range(aliens_per_column):
            for alien_number in range(aliens_per_row):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self.screen)
        alien_width, alien_height = alien.rect.size
        alien.position_x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.position_x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def increase_game_speed(self):
        self.settings.increase_speed()
