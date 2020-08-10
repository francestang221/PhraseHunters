# Create your Character class logic in here.


class Character:
    """Represents a single character"""
    def __init__(self, char, was_guessed=False):
        self.char = char
        self.was_guessed = was_guessed

    def show_char(self):
        if self.was_guessed or self.char == " ":
            print(self.char, end="")
        else:
            print("_", end="")

    def check_guess(self, guess):
        if guess == self.char:
            self.was_guessed = True



