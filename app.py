# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop


from phrasehunter.character import Character
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase

import random


def main():
    game1 = Game()
    game1.startGame()

    phrase1 = Phrase("just do it")
    phrase2 = Phrase("cash is king")
    phrase3 = Phrase("cat in a hat")

    def guess_game():
        random_phrases = [phrase1, phrase2, phrase3]
        x = int(random.randint(1, len(random_phrases)))

        target = random_phrases[x - 1]

        # show the blank lines
        for letter in target:
            if letter != " ":
                print("_", end="")
            if letter == " ":
                print(" ", end="")
        tar = list(target)

        # guess

        while x < len(tar):
            guess = input("\n\nGuess a letter: ")
            for letter in target:
                if guess == letter:
                    print(guess, end="")
                if guess != letter and not Character.get_was_guessed(letter):
                    print("_", end="")
                if letter == " ":
                    print(" ", end="")
            x += 1


    guess_game()


if __name__ == '__main__':
    main()