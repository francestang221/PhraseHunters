# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop


from phrasehunter.game import Game


if __name__ == '__main__':
    phrases = ["just do it", "python is fun", "cat in a hat"]
    game = Game(phrases)
    game.start_game()