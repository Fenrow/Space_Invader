import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """Klasa przeznaczona do wyświetlania punktacji oraz innych informacji o grze"""

    def __init__(self, ai_settings, screen, stats):
        """Inicjalizacja atrybutów dotyczących punktacji"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Ustawienie czcionki dla informacji dotyczących punktacji
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 32)

        #Przygotowanie początkowych obrazów z punktacją
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Przekształcenie punktacji w obraz do wyświetlenia"""

        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #Wyświetlenie punktacji w prawym górnym rogu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Przekształcenie najwyżeszego wyniku w obraz do wyświetlenia"""

        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        #Wyświetlenie najelepszego wyniku na środku ekranu przy górnej krawędzi
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """Przekształcenie aktualnego poziomu na obraz do wyświetlenia"""

        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        #Numer poziomu jest wyświetlany pod aktualną punktacją
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Wyświetla liczbę statków jakie pozostały graczowi"""

        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Wyświetlanie punktacji na ekranie"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        #Wyświetlenie staktów(żyć)
        self.ships.draw(self.screen)
