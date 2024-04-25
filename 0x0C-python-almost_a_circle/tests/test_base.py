#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Test case for Base class"""

    def test_auto_id(self):
        """Test Base class id management"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_None(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)



if __name__ == "__main__":
    unittest.main()
