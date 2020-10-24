import unittest
import arrproblems.stringcompress as a


class TestCompress(unittest.TestCase):

    def test_compress(self):
        self.assertEqual(a.compress("AAAABBBBCCCCCDDEEEE"), 'A4B4C5D2E4')
        self.assertEqual(a.compress(''), '')
        self.assertEqual(a.compress('AABBB'), 'A2B3')
        print("Passed!!!!!!!!!!!!!!!!")



if __name__ == "__main__":
    unittest.main()