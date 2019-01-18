import unittest
from exercises import hackerrank


class TestDiagonalDifference(unittest.TestCase):
    """ 
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    https://www.hackerrank.com/challenges/diagonal-difference/problem
    """
    def setUp(self):
        """ Setting up for the test """
        self.arr = ( (11,  2,   4), 
                     ( 4,  5,   6),
                     (10,  8, -12) )
    
    def test_dd(self):
        """ testing happy path diagonal diference """
        self.assertEqual(hackerrank.diagonalDifference(self.arr), 15)
            

if __name__ == '__main__':
    unittest.main()