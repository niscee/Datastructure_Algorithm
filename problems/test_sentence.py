import unittest
import arrproblems.sentence as a


class Testreversal(unittest.TestCase):

    def test_reversal(self):
        self.assertEqual(a.reversal('   space before'), 'before space')
        self.assertEqual(a.reversal('space after   '), 'after space')
        self.assertEqual(a.reversal('  Hello John    how are you    '), 'you are how John Hello')
        print("ALL TEST CASES PASSED")



if __name__ == "__main__":
    unittest.main()        