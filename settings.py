class Settings:
    """A class to store all setting for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game's statics settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 20

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly hte alien point value increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initilize settings that change throuhout the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.3
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)
