import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Inwazja Obcych')

    #Utworzenie statku kosmicznego
    ship = Ship(ai_settings, screen)

    #Rozpoczęcie pętli głównej gry
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
