"""This is the main test class."""

import unittest
from hsanagrams.anagrams import Anagrams

class TestAnagrams(unittest.TestCase):
    """Main test class"""
    #def __init__(self):
    #    self.wordspath = "test/words.txt"

    def test_anagrams(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertEqual(anagrams.get_anagrams('plates'),
                        ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

    #def test_anagrams1(self):
    #    """Dummy Test"""
    #    self.assertEqual(1, 1)

def run_all():
    """Run all Test"""
    unittest.main()

if __name__ == "__main__":
    run_all()
