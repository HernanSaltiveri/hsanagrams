"""This is the main test class."""
import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from hsanagrams.anagrams import Anagrams

class TestAnagrams(unittest.TestCase):
    """Main test class"""
    #anagrams = []

    #@classmethod
    #def setUpClass(cls):
    #    cls.anagrams = Anagrams("test/words.txt")

    def test_anagram_plates(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertEqual(anagrams.get_anagrams('plates'),
                        ['palest', 'pastel', 'petals', 'plates', 'staple'])

    def test_anagram_eat(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

    def test_anagram_boa(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertEqual(anagrams.get_anagrams('boa'), ['Abo', 'boa'])

    def test_anagram_act(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertEqual(anagrams.get_anagrams('act'), ['act', 'cat'])

    def test_anagram_ads(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertEqual(anagrams.get_anagrams('ads'), ['ads', 'sad'])

    def test_anagram_eath(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertEqual(anagrams.get_anagrams('earth'), ['earth', 'hater', 'heart'])

    def test_anagram_eath2(self):
        """First Test"""
        anagrams = Anagrams("test/words.txt")
        self.assertNotEqual(anagrams.get_anagrams('earth'), ['earth', 'hater'])

def run_all():
    """Run all Test"""
    unittest.main()

if __name__ == "__main__":
    run_all()
