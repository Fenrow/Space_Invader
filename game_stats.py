import json

class GameStats():
    """Monitorowanie danych statystycznych w grze"""

    def __init__(self, ai_settings):
        """Inicjalizacja danych statystycznych"""

        self.ai_settings = ai_settings
        self.reset_stats()

        #Stan gry
        self.game_active = False

        #Próba otworzenia pliku z najwyższym wynikiem jeśli nie istnieje
        #Wyzerowanie wyniku
        try:
            with open(self.ai_settings.fname_high_score) as fname:
                self.high_score = json.load(fname)
        except FileNotFoundError:
            #Najlepszy wynik
            self.high_score = 0

        #Bieżący poziom
        self.level = 1

    def reset_stats(self):
        """Inicjalizacja danych statystycznych które mogą zmieniać się
        podczas gry"""

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
