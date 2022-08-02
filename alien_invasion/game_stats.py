class GameStats:
    def __init__(self, game):
        self.settings = game.settings
        self.high_score = 0
        self.level = 1
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
