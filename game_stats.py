class GameStats():
    """Monitorowanie danych statystycznych w grze"""

    def __init__(self, ai_settings):
        """Inicjalizacja danych statystycznych"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Inicjalizacja danych statystycznych które mogą zmieniać się podczas gry"""
        self.ships_left = self.ai_settings.ship_limit
