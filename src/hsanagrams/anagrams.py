"""This is the main logic class."""
class Anagrams: # pylint: disable=R0903
    """Logic"""
    def __init__(self, wordsfile):
        """Init"""
        with open(wordsfile, "r") as file: # pylint: disable=W1514
            self.words = file.read().splitlines()

    def get_anagrams(self, targetword):
        """Get Anagrams for word from list"""
        target_key = sorted(targetword.lower())
        matches = [word for word in self.words if sorted(word.lower()) == target_key]
        return matches
