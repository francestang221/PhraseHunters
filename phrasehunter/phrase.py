from phrasehunter.character import Character


class Phrase:
    """ Represents a Phrase object"""
    def __init__(self, phrase):
        """ Initializes a Phrase object """
        self.phrase = []  # a collection of Character objects
        for char in phrase:
            self.phrase.append(Character(char))
        self.all_char_guessed = False

    def show_phrase(self):
        """ Prints out a phrase"""
        for char in self.phrase:
            print(char.show_char(), end="")

    def check_guess(self, guess):
        """Checks if the guess matches any character in the phrase """
        for char in self.phrase:
            char.update_guess(guess)

    def guessed_char(self):
        """ Returns the number of characters have been guessed in the phrase """
        guessed_char = 0
        for char in self.phrase:
            if char.was_guessed is True:
                guessed_char += 1
        return guessed_char

    def goal_guess(self):
        """ Returns the maximum number of characters that can be guessed in the phrase """
        goal = 0
        for char in self.phrase:
            if Character.get_char(char) != " ":
                goal += 1
        return goal

    def all_guessed(self):
        """
        Return True if all characters in the phrase have been guessed
        Returns False if otherwise
        """
        if self.goal_guess() == self.guessed_char():
            return True
        else:
            return False

    def reset_phrase(self):
        """
        Resets the guess status for all the characters in the phrase back to False
        """
        for char in self.phrase:
            Character.reset_guessed(char)





