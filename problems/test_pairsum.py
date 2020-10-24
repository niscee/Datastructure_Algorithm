import unittest
import arrproblems.arraypair as a


class TestArray(unittest.TestCase):

    def test_pair_sum(self):
        self.assertEqual(a.pair_sum([1,3,2,2],4), 2)
        self.assertEqual(a.pair_sum([1,2,3,1],3), 1)
        self.assertEqual(a.pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        print("ALL TEST CASES PASSED")



if __name__ == "__main__":
    unittest.main()        