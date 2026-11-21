"""This is the main test class."""

import unittest
from hsanagrams.anagrams import Anagrams

class TestAnagrams(unittest.TestCase):
    """Main test class"""
    
    anagrams = []

    @classmethod
    def setUpClass(cls):
        cls.anagrams = Anagrams("test/words.txt")    

    def test_anagram_plates(self):
        """First Test"""
        #anagrams = Anagrams("test/words.txt")
        self.assertEqual(self.anagrams.get_anagrams('plates'),
                        ['palest', 'pastel', 'petals', 'plates', 'staple'])

    def test_anagram_eat(self):
        """First Test"""
        #anagrams = Anagrams("test/words.txt")
        self.assertEqual(self.anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

def run_all():
    """Run all Test"""
    unittest.main()

if __name__ == "__main__":
    run_all()
