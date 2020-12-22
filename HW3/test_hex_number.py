import unittest

from HW3.hex_number import HexNumber


class TestHexNumber(unittest.TestCase):

    def test_not_empty(self):
        num = HexNumber('0')
        self.assertIsNotNone(num.head)

    def test_negative(self):
        self.assertRaises(ValueError, HexNumber, '-A3')

    def test_hex_number(self):
        self.assertRaises(ValueError, HexNumber, 'Z4A')

    def test_upper_case(self):
        self.assertRaises(ValueError, HexNumber, 'a4')

    def test_add_zero(self):
        num = '3C'
        num1 = HexNumber('0')
        num2 = HexNumber(num)
        num3 = num2.add(num1)
        self.assertEqual(num, str(num3))

    def test_add(self):
        num1 = HexNumber('A')
        num2 = HexNumber('1B')
        num3 = num1.add(num2)
        num4 = num2.add(num1)
        self.assertEqual('25', str(num3))
        self.assertEqual(str(num3), str(num4))
