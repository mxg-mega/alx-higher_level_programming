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
        self.assertEqual(r2.id, 5)

        r3 = Rectangle()
        self.assertEqual(r3.id, 6)

    def test_custom_id(self):
        r1 = Rectangle(1, 1, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_None(self):
        r1 = Rectangle(1, 1, 0, 0, None)
        self.assertEqual(r1.id, 4)

    def test_attributes(self):
        r1 = Rectangle(6, 5, 45, 4, 34)
        self.assertEqual(r1.id, 34)
        self.assertEqual(r1.x, 45)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 5)

    def test_getter_setter(self):
        r1 = Rectangle(1, 1, 0, 0, 45)
        r1.width = 23
        self.assertEqual(r1.width, 23)
        r1.height = 12
        self.assertEqual(r1.height, 12)
        r1.x = 5
        self.assertEqual(r1.x, 5)
        r1.y = 2
        self.assertEqual(r1.y, 2)

    def test_raises(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 1, 0, 0, 0)
            r2 = Rectangle(1, -1, 0, 0, 0)
            r3 = Rectangle(1, 1, -1, 0, 0)
            r4 = Rectangle(1, 1, 0, -1, 0)

        with self.assertRaises(TypeError):
           r1 = Rectangle("0", 1, 0, 0, 0)
           r2 = Rectangle(1, "height", 0, 0, 0)
           r3 = Rectangle(1, 1, "x", 0, 0)
           r4 = Rectangle(1, 1, 0, "y", 0)



if __name__ == "__main__":
    unittest.main()
