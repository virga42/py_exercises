import unittest
from sample import addition

class TestOperators(unittest.TestCase):
    def test_additon(self):
        self.assertEqual(addition(1, 2), 3)

if __name__ == '__main__':
    unittest.main()