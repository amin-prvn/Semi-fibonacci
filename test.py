import unittest
from app import sequence


class TestFibonacciSequence(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(sequence(0), 0)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(6), 8)
        self.assertEqual(sequence(10), 10)
        self.assertEqual(sequence(11), 8)
        self.assertEqual(sequence(12), 9)

if __name__ == '__main__':
    unittest.main()