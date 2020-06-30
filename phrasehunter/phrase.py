# Create your Phrase class logic here.


from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase, all_guessed=False):
        self.phrase = phrase  # a collection of Char
        self.all_guessed = all_guessed

    def sample(self, c):
        Character.show_char(c, "a")