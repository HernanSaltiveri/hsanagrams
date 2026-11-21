"""This is the main logic class."""

class Anagrams:

    def __init__(self, wordsfile):
        with open(wordsfile, "r") as file:
            self.words = file.read().splitlines()

    def get_anagrams(self, targetword):
        """Get Anagrams for word from list"""
        target_key = sorted(targetword.lower())
        matches = [word for word in self.words if sorted(word.lower()) == target_key]
        return matches
