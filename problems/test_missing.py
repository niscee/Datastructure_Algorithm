import unittest
from arrproblems import missingelement


class Testmissing(unittest.TestCase):

    def test_missing(self):
        self.assertEqual(missingelement.finder([5,5,7,7],[5,7,7]),5)
        self.assertEqual(missingelement.finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        self.assertEqual(missingelement.finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print("Passed!!!!!!!!")




if __name__ == "__main__":
    unittest.main()        