#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """ """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([1]), 1)
        self.assertIsNone(max_integer())

    def test_max_integer_raises(self):
        """"""
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, float("nan"))
        self.assertRaises(TypeError, max_integer, "list")
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, [1, "2", 3])

if __name__ == '__main__':
    unittest.main()
