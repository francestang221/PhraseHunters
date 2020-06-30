# Create your Character class logic in here.


class Character:
    """Represents a single character"""
    def __init__(self, char="_", char_guessed=False):
        self.char = char
        self.char_guessed = char_guessed

    def update_guess(self, char):
        if char in phrase:
            self.char_guessed = True

    def show_char(self, char):
        if self.char_guessed:
            self.char = char




