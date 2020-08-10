# Create your Game class logic in here.


class Game:
    def __init__(self, game_on=False):
        self.game_on = game_on

    def startGame(self):
        print("\nWelcome to the Phrase Hunters Game! \n")

    def askPlayer(self):
        input("Guess a letter: ")

    def game_result(self, win=False):
        while self.game_on:
            if win:
                print("Congrats! You won!")
            else:
                print("Oh well...Better luck next time!")

