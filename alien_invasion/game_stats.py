class GameStats:
    """
    Provides the game stats for the Alien Invasion game.

    Used by the Model class.
    """

    def __init__(self, ship_limit):
        self.high_score = 0
        self.game_active = False
        self.reset_stats(ship_limit)

    def reset_stats(self, ship_limit):
        self.ships_left = ship_limit
        self.level = 1
        self.score = 0
