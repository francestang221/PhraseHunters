# Create your Character class logic in here.


class Character:
    """Represents a single character"""
    def __init__(self, char="_", was_guessed=False):
        self.char = char
        self.was_guessed = was_guessed

    def get_was_guessed(self):
        return self.was_guessed

    def update_guess(self):
        self.was_guessed = True

    def show_char(self, char):
        if self.was_guessed:
            self.char = char




