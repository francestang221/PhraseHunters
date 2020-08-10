# Create your Character class logic in here.


class Character:
    """Represents a single character"""
    def __init__(self, char, was_guessed=False):
        self.char = char
        self.was_guessed = was_guessed

    def get_char(self):
        """ Returns the char data"""
        return self.char

    def show_char(self):
        """
        Returns the char data if the char was guessed or is a space
        Returns an underscore if otherwise
        """
        if self.was_guessed or self.char == " ":
            return self.char
        else:
            return "_"

    def update_guess(self, guess):
        """
        Updates the guess status to True if the guess matches the char
        """
        if guess == self.char:
            self.was_guessed = True

    def reset_guessed(self):
        """ Resets the char's guess status to False"""
        self.was_guessed = False



