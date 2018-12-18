class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry"""

    def __init__(self):
        """inicjalizacja ustawień gry"""
        #Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ustawienia statku
        self.ship_speed_factor = 1.5

        #Ustawienia pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 30, 30)
        self.bullets_allowed = 5
