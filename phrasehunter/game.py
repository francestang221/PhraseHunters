# Create your Game class logic in here.

from phrasehunter.character import Character
from phrasehunter.phrase import Phrase
import random


class Game:
    def __init__(self, phrase_list):
        self.phrase_list = [Phrase(phrase) for phrase in phrase_list]
        self.target_phrase = random.choice(self.phrase_list)
        self.chances = 5
        self.win = False

    def start_game(self):
        print("\nWelcome to the Phrase Hunters Game! \n")
        self.new_game()

    def new_game(self):
        correct_guesses_so_far = 0

        while self.chances > 0:
            Phrase.show_phrase(self.target_phrase)
            print("\n")
            guess = input("Guess a letter: ")
            if len(guess) != 1:
                guess = input("\nnot a valid guess. try again: ")

            Phrase.validate_guess(self.target_phrase, guess)
            if Phrase.guessed_char(self.target_phrase) == correct_guesses_so_far:
                self.chances -= 1
                print("\n~~~You have {} out 5 lives remaining.~~~~\n".format(self.chances))
            else:
                print("\nGood job!\n")
                correct_guesses_so_far = Phrase.guessed_char(self.target_phrase)




        self.display_result()

    def display_result(self):
        if self.win:
            print("Congratulations! You won!")
        else:
            print("You lost...Better luck next time!")







