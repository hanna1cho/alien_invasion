class Settings:

    def __init__(self):
        """initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (0, 0, 0)

        #ship settings
        # self.ship_speed = 3.0
        self.ship_limit = 3

        #bullet settings
        # self.bullet_speed = 2.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

        #alien settings
        # self.alien_speed = 1.0
        # do not need to change the fleet drop speed below because when aliens move faster, fleet will also drop faster
        self.fleet_drop_speed = 15
        #fleet direction of 1 represents right; -1 represents left
        # self.fleet_direction = 1

        #how quickly the game speeds up
        self.speedup_scale = 1.2

        #how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)