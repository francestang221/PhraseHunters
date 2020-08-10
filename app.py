from phrasehunter.game import Game


def main():
    phrases = ["just do it", "python is fun", "cat in a hat", "cash is king", "love is patience"]
    game = Game(phrases)
    game.start_game()


if __name__ == '__main__':
    main()
