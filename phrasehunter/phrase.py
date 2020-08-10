# Create your Phrase class logic here.


from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = []  # a collection of Character objects
        for letter in phrase:
            self.phrase.append(Character(letter))


