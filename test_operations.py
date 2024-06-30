import unittest
from operations import (
    sumar,
    sub,
    mul,
    div
)

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(sub(3, 2), 1)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1, -1), 0)

class TestMul(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul(3, 2), 6)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(-1, -1), 1)
        self.assertEqual(mul(0, 3), 0)
        self.assertEqual(mul(7, 0), 0)
        self.assertEqual(mul(-7, 0), 0)

class TestDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(div(3, 2), 1.5)
        self.assertEqual(div(-1, 1), -1)
        self.assertEqual(div(-1, -1), 1)
        self.assertEqual(div(0, 5), 0)
    
    def test_zero_div(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertRaises(div(11, 0), ValueError)

        with self.assertRaises(ZeroDivisionError):
            self.assertRaises(div(11, 0), ValueError)

if __name__ == "__main__":
    unittest.main()