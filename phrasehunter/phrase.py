# Create your Phrase class logic here.


from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = []  # a collection of Character objects
        for letter in phrase:
            self.phrase.append(Character(letter))
        self.all_char_guessed = False

    def show_phrase(self):
        for char in self.phrase:
            char.show_char()

    def validate_guess(self, guess):
        for char in self.phrase:
            char.check_guess(guess)

    def guessed_char(self):
        guessed_char = 0
        for char in self.phrase:
            if char.was_guessed is True:
                guessed_char += 1
        return guessed_char






