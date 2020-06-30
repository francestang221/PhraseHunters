# Create your Game class logic in here.


class Game:
    def __init__(self, game_on=False):
        self.game_on = game_on


    def startGame(self):
        return None

    def askPlayer(self):
        input("Guess a character: ")

    def result(self):
        # win or loss

