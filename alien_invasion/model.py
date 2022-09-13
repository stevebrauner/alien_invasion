from game_stats import GameStats
from settings import ModelSettings


class Model:
    """
    The Model for the Alien Invasion game.

    The Model uses the ModelSettings and GameStats classes to hold
    the data.
    """

    def __init__(self):
        self.settings = ModelSettings()
        self.stats = GameStats(self.settings.ship_limit)

    def initialize_dynamic_settings(self):
        self.settings.initialize_dynamic_settings()

    def increase_points(self):
        self.settings.increase_points()

    def set_game_active(self, flag):
        self.stats.game_active = flag

    def get_game_active(self):
        return self.stats.game_active

    def get_score(self):
        return self.stats.score

    def set_score(self, score):
        self.stats.score = score

    def get_high_score(self):
        return self.stats.high_score

    def set_high_score(self, high_score):
        self.stats.high_score = high_score

    def get_level(self):
        return self.stats.level

    def set_level(self, level):
        self.stats.level = level

    def get_ships_left(self):
        return self.stats.ships_left

    def set_ships_left(self, ships_left):
        self.stats.ships_left = ships_left

    def get_ship_speed(self):
        return self.settings.ship_speed

    def get_alien_points(self):
        return self.settings.alien_points

    def reset_model(self):
        self.stats.reset_stats(self.settings.ship_limit)
