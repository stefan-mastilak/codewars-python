"""

Task definition:
----------------
1) Create RGB to HEX converter function taking 3 integers for red green and blue as an input.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

2) Create reverse converter to rgb taking hex code string as an input. R
Reverse converter should return RGB as a tuple.

The following are examples of expected output values:

Examples:
---------
rgb_to_hex(255, 255, 255)   -->  '#FFFFFF'
rgb_to_hex(255, 255, 300)   -->  '#FFFFFF'
rgb_to_hex(0,0,0)           -->  '#000000'
rgb_to_hex(148, 0, 211)     -->  '#9400D3'

hex_to_rgb('#9400D3')       -->  (148, 0, 211)
hex_to_rgb('#FFFFFF')       -->  (255, 255, 255)
hex_to_rgb('#000000')       -->  (0, 0, 0)
hex_to_rgb('#FEFDFC')       -->  (254, 253, 252)

"""

import unittest


def rgb_to_hex(r: int, g: int, b: int):
    """
    RGB to HEX converter
    :param r: red (integer 0-255)
    :param g: green (integer 0-255)
    :param b: blue (integer 0-255)
    :return: Hex code as string
    :rtype: string
    """
    def validator(inpt):
        if inpt < 0:
            return 0
        elif inpt > 255:
            return 255
        else:
            return inpt
    return '#{:02x}{:02x}{:02x}'.format(validator(r), validator(g), validator(b)).upper()


def hex_to_rgb(hex_code: str):
    """
    HEX to RGB converter
    :param hex_code: hex code as string (starting with #)
    :return: rgb code as tuple
    :rtype: tuple
    """
    return tuple(int(hex_code.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))


class TestRgbToHex(unittest.TestCase):
    """
    Test - RGB to HEX conversion 
    """
    def test1(self):
        self.assertEqual("#000000", rgb_to_hex(0, 0, 0))

    def test2(self):
        self.assertEqual("#FFFFFF", rgb_to_hex(255, 255, 255))

    def test3(self):
        self.assertEqual("#FEFDFC", rgb_to_hex(254, 253, 252))

    def test4(self):
        self.assertEqual("#00FF7D", rgb_to_hex(-20, 275, 125), "testing out of range values")

    def test5(self):
        self.assertEqual("#0000FF", rgb_to_hex(-3000, 0, 800), "testing out of range values")


class TestHexToRgb(unittest.TestCase):
    """
    Test - HEX to RGB conversion
    """
    def test1(self):
        self.assertEqual((0, 0, 0), hex_to_rgb('#000000'))

    def test2(self):
        self.assertEqual((254, 253, 252), hex_to_rgb('#FEFDFC'))

    def test3(self):
        self.assertEqual((1, 2, 3), hex_to_rgb('#010203'))

    def test4(self):
        self.assertEqual((0, 0, 255), hex_to_rgb('#0000FF'))

    def test5(self):
        self.assertEqual((255, 255, 255), hex_to_rgb('#FFFFFF'))


if __name__ == '__main__':
    unittest.main()
