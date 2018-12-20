import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():

    #Inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Inwazja Obcych')
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Utworzenie statku kosmicznego
    ship = Ship(ai_settings, screen)

    #Utworzenie grupy przeznaczonej do przechowywania pocisków
    bullets = Group()

    #Utworzenie grupy przeznaczonej do przechowywania obcych
    aliens = Group()

    #Utworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Utworzenie przycisku Gra
    play_button = Button(200, 50, ai_settings, screen, 'Gra')

    #Rozpoczęcie pętli głównej gry
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
