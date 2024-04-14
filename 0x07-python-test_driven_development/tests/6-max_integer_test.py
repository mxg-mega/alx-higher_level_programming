#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """ """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-11, 3, 5, 8]), 8)
        self.assertEqual(max_integer([-1, 0]), 0)
        self.assertEqual(max_integer([1.5, 0.4, 5.2]), 5.2)
        self.assertEqual(max_integer([1, 2, 3, 1.5, 2.5]), 3)
        self.assertEqual(max_integer([500, 200, 45, 100]), 500)
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
