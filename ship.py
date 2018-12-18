import pygame

class Ship():
    """Klasa odpowiedzialna za statek gracza"""

    def __init__(self, ai_settings, screen):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""

        self.screen = screen
        self.ai_settings = ai_settings

        #Wczytywanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Każdy nowy statek pojawia się na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Punkt środkowy statku jest przechowywany w postaci liczby zmiennoprzecinkowej
        self.center = float(self.rect.centerx)

        #Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Wyświetlenie statku w aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego
        ruch"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        #uaktualnienie obiektu rect na podstawie wartości self.center
        self.rect.centerx = self.center
