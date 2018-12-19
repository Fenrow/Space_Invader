class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry"""

    def __init__(self):
        """inicjalizacja ustawień gry"""
        #Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ustawienia statku
        self.ship_limit = 3

        #Ustawienia pocisku
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 102, 0)
        self.bullets_allowed = 4

        #Ustawienia obcego
        self.fleet_drop_speed = 10

        #Łatwa zmiana szybkości gry
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień zmieniających się podczas gry"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1 #Wartość 1 --> Wartość -1 <--

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
