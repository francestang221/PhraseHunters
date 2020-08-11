from phrasehunter.phrase import Phrase
import random


class Game:
    """ Represents a Game object """

    def __init__(self, phrase_list):
        self.phrase_list = [Phrase(phrase) for phrase in phrase_list]
        self.target_phrase = random.choice(self.phrase_list)
        self.chances = 5
        self.win = False

    def start_game(self):
        """ Prints out a welcome message and start the game """
        print("\n>>> Welcome to the Phrase Hunters Game! <<<\n")
        self.new_game()

    def new_game(self):
        """
        Prompts the player to guess a letter
        Ends the game when the game is won
        or all the chances have been used
        Asks the player if they want to play again
        """

        correct_guesses_so_far = 0
        guessed = []

        while not self.target_phrase.all_guessed():

            if self.chances < 1:
                self.win = False
                break

            else:
                self.target_phrase.show_phrase()
                print("\n")
                guess = input("Guess a letter: ")

                while len(guess) > 1 or guess.isalpha() is False:
                    guess = input("\nnot a valid guess. try again: ")

                self.target_phrase.check_guess(guess)

                if self.target_phrase.guessed_char() == correct_guesses_so_far:
                    if guess not in guessed:
                        self.chances -= 1
                        print("\n>>> You have {} out 5 lives remaining. <<< \n".format(self.chances))
                    else:
                        print("\nYou already guessed this letter. Try a different one. \n")
                else:
                    guessed.append(guess)
                    print("\n>>> Good job! <<< \n")
                    correct_guesses_so_far = self.target_phrase.guessed_char()

        if self.target_phrase.all_guessed():
            self.win = True

        self.display_result()

    def display_result(self):
        """
        Prints out the message depending on the game result
        Asks the player to play again
        """
        if self.win:
            print(">>> Congratulations! You won! <<<")
        else:
            print(">>> You lost...Better luck next time! <<<")
        self.play_again()

    def reset(self):
        """
        Resets the game data
        """
        self.target_phrase = random.choice(self.phrase_list)
        self.chances = 5
        self.win = False
        self.target_phrase.reset_phrase()

    def play_again(self):
        """
        Asks the player if they want to play again
        Restart the game if yes
        Print a farewell message if otherwise
        """
        answer = input("\nWould you like to play another round? Press 'Y' to play or any other key to quit: \n")

        if answer.lower() == "y":
            self.reset()
            self.start_game()

        else:
            print("\n >>> See you next time! <<< ")














