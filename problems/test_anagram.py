import unittest
import arrproblems.anagram as a

class Testanagarm(unittest.TestCase):

    def test_anagram(self):
        result = a.anagramCheck("dog", "god")
        self.assertEqual(result, True)