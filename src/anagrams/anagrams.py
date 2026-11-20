import unittest

class Anagrams:

    def __init__(self, wordsfile):
        self.words = open(wordsfile).read().splitlines()

    def get_anagrams(self, targetword):
        target_key = sorted(targetword.lower())
        matches = [word for word in self.words if sorted(word.lower()) == target_key]
        return matches
        