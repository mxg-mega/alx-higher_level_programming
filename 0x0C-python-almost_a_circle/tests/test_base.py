#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


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




class TestRecangle_instantiation(unittest.TestCase):
    """Test case for Base class"""

    def test_auto_id(self):
        """Test Base class id management"""
        r2 = Rectangle()
        self.assertEqual(r2.id, 4)

        r3 = Rectangle()
        self.assertEqual(r3.id, 5)

    def test_custom_id(self):
        r1 = Rectangle(0, 0, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_None(self):
        r1 = Rectangle(None)
        self.assertEqual(r1.id, 7)

    def test_attributes(self):
        r1 = Rectangle(6, 5, -4, 4, 34)
        self.assertEqual(r1.id, 34)
        self.assertEqual(r1.x, -4)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 5)


if __name__ == "__main__":
    unittest.main()
