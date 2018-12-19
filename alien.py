import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa opisująca obcego"""

    def __init__(self, ai_settings, screen):
        """Inicjalizacja Obcego i jego położenie początkowe"""

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Wczytanie obrazu obcego i pobranie jego prostokąta
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Umieszczenie nowego obcego w pobliży lewego górnego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Przechowanie dokładnego położenia Obcego
        self.x = float(self.rect.x)

    def blitme(self):
        """Wyświetlanie obcego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)
