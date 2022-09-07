import sys
from time import sleep

import pygame


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def run(self):
        while True:
            self._check_events()

            self._update_view()
            self._initialize_scoreboard()
            self.view.update_screen(self.model.get_game_active())

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.view.set_ship_moving_right(True)
        elif event.key == pygame.K_LEFT:
            self.view.set_ship_moving_left(True)
        elif event.key == pygame.K_SPACE:
            self.view.fire_bullet()
        elif event.key == pygame.K_p:
            if not self.model.get_game_active():
                self._start_game()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.view.set_ship_moving_right(False)
        elif event.key == pygame.K_LEFT:
            self.view.set_ship_moving_left(False)

    def _check_play_button(self, mouse_position):
        button_clicked = self.view.was_button_clicked(mouse_position)
        if button_clicked and not self.model.get_game_active():
            self._start_game()

    def _start_game(self):
        self.model.initialize_dynamic_settings()
        self.model.reset_model()
        self._initialize_scoreboard()
        self.model.set_game_active(True)
        self.view.reset_view()
        pygame.mouse.set_visible(False)

    def _initialize_scoreboard(self):
        self.view.prep_score(self.model.get_score())
        self.view.prep_high_score(self.model.get_high_score())
        self.view.prep_level(self.model.get_level())
        self.view.prep_ships_left(self.model.get_ships_left())
        self.view.draw_scoreboard()

    def _update_view(self):
        if self.model.get_game_active():
            self.view.update_ship(self.view.get_ship_speed())
            self.view.update_bullets()
            hits = self.view.check_and_get_bullet_alien_hits()
            if hits:
                for aliens in hits.values():
                    self.model.set_score(
                        self.model.get_score()
                        + self.model.get_alien_points() * len(aliens)
                    )
                self.view.prep_score(self.model.get_score())
                self._check_high_score()
            if not self.view.get_aliens():
                self.view.bullets.empty()
                self.view.create_fleet()
                self.view.increase_game_speed()
                self.model.set_level(self.model.get_level() + 1)
                self.view.prep_level(self.model.get_level())
            self.view.update_aliens()
            if self.view.is_ship_hit():
                self._decrement_ship_and_pause_or_end()
            if self.view.has_alien_hit_bottom():
                self._decrement_ship_and_pause_or_end()

    def _check_high_score(self):
        if self.model.get_score() > self.model.get_high_score():
            self.model.set_high_score(self.model.get_score())
            self.view.prep_high_score(self.model.get_high_score())

    def _decrement_ship_and_pause_or_end(self):
        if self.model.get_ships_left() > 0:
            self.model.set_ships_left(self.model.get_ships_left() - 1)
            sleep(0.5)
        else:
            self.model.set_game_active(False)
            pygame.mouse.set_visible(True)
