# Create your Phrase class logic here.


from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = []  # a collection of Character objects
        for char in phrase:
            self.phrase.append(Character(char))
        self.all_char_guessed = False

    def show_phrase(self):
        for char in self.phrase:
            print(char.show_char(), end="")

    def validate_guess(self, guess):
        for char in self.phrase:
            char.check_guess(guess)

    def guessed_char(self):
        guessed_char = 0
        for char in self.phrase:
            if char.was_guessed is True:
                guessed_char += 1
        return guessed_char

    def goal_guess(self):
        goal = 0
        for char in self.phrase:
            if Character.get_char(char) != " ":
                goal += 1
        return goal

    def all_guessed(self):
        if self.goal_guess() == self.guessed_char():
            return True
        else:
            return False






