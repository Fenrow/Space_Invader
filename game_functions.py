import sys
import pygame
from time import sleep
import json

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Reakcja na naciśnięcie klawisza"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        save_high_score(ai_settings, stats)
        sys.exit()

    elif event.key == pygame.K_g:
        start_game(ai_settings, screen, stats, sb, True, ship, aliens, bullets)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Rozpoczęcie nowej gry po wciśnięciu przycisku gra"""

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    start_game(ai_settings, screen, stats, sb, button_clicked, ship, aliens, bullets)

def start_game(ai_settings, screen, stats, sb, button_clicked, ship, aliens, bullets):
    """Rozpoczęcie nowej gry"""

    if button_clicked and not stats.game_active:
        #Ustawienie wartości początkowych dla wartości prędkości
        ai_settings.initialize_dynamic_settings()

        #Ukrycie kursowra myszy
        pygame.mouse.set_visible(False)

        #Wyzerowanie danych statystycznych gry
        stats.reset_stats()
        stats.game_active = True

        #Wyzerowanie obrazów tablicy wyników
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Usunięcie zawartości list aliens i bullets
        aliens.empty()
        bullets.empty()

        #Utworzenie nowej floty i wyśrodkowanie statku gracza
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_keyup_events(event, ship):
    """Reakcja na zwolnienie klawisza"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Reakcja na zdarzenia generowane przez klawiature i mysz"""

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            save_high_score(ai_settings)
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu"""

    #Odświeżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)

    #Wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego i Obcych
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Wyświetlanie informacji o punktacji
    sb.show_score()

    #Wyświetlanie przycisku tylko wtedy gdy gra jest nieaktywna
    if not stats.game_active:
        play_button.draw_button()

    #Wyświetlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych
     na ekranie"""

    #Uaktualnienie położenia pocisków
    bullets.update()

    #Usunięcie pocisków, które znajdują się poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    chceck_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)

def chceck_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):

    #Sprawdzenie kolizji między pociskiem a obcym
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:

        #Jeżeli gracz zniszczył całą flotę przechodzi na kolejny poziom
        bullets.empty()
        ai_settings.increase_speed()

        #inkrementacja numeru poziomu i wyświetlenie go
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Wystrzelenie pocisku jeśli nie przekroczono ustalonego limitu"""

    #Utworzenie nowego pocisku i dodanie go do grupy pocisków
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Ustalenie maksymalnej liczby obcych w rzędzie"""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Utworzenie obcego i umieszczenie go w rzędzie"""

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Utworzenie floty obcych"""

    #Utworzenie obcego i ustalenie liczby obcych którzy zmieszczą się na ekranie
    #Odległość między obcymi jest równa szerokości Obcego
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
    alien.rect.height)

    #Utworzenie rzędu obcych
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Ustalenie liczby rzędów obcych które zmieszczą się na ekranie"""

    available_space_y = (ai_settings.screen_height -
    (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def chceck_fleet_edges(ai_settings, aliens):
    """Reakcja gdy obcy dotrze do krawędzi ekranu"""

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Przesunięcie floty w dół i zmiana kierunku"""

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Uaktualnienie położenia obcych"""

    chceck_fleet_edges(ai_settings, aliens)
    aliens.update()

    #Wykrywanie kolizji między obcym a statkiem gracza
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    chceck_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Reakcja na uderzenie obcego w statek"""

    if stats.ships_left > 0:
        #Zmienjszenie wartości przechowywanej w ships_left
        stats.ships_left -= 1

        #Uaktualnienie tablicy statków (żyć)
        sb.prep_ships()

        #Usunięcie zawartości list aliens i bullets
        aliens.empty()
        bullets.empty()

        #Utworzenie nowej floty i wyśrodkowanie statku
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #Pauza
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def chceck_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Sprawdzenie czy którykolwiek obcy dotarł do dolnej krawędzi ekranu"""

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """Sprawdzenie czy mamy nowy najlepszy wynik w grze"""

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def save_high_score(ai_settings, stats):
    """Zapisanie najwyżeszego wyniku do pliku"""

    with open(ai_settings.fname_high_score, 'w') as fname:
        json.dump(stats.high_score, fname)
