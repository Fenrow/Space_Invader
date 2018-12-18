import sys
import pygame

def check_events(ship):
    """Reakcja na zdarzenia generowane przez klawiature i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #przesunięcie statku w prawą stronę
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                #przesunięcie statku w lewą stronę
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""
    #Odświeżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Wyświetlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()
