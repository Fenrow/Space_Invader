import sys
import pygame

def check_events():
    """Reakcja na zdarzenia generowane przez klawiature i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""
    #Odświeżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Wyświetlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()
