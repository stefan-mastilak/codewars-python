# REF: stefan.mastilak@gmail.com

"""

Task definition:
----------------
In this task you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

Example:
--------
input >> alphabet_position("The sunset sets at twelve o' clock.")
output >> "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

"""

import unittest
from string import ascii_lowercase


def alphabet_position(text: str):
    """
    Function will return string with alphabet position of the letters in text
    :param text: input string
    :return: alphabet position of the letters in text
    :rtype: str
    """
    return ' '.join(str(ascii_lowercase.index(i.lower()) + 1) for i in text if i.isalpha())


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_string = "The sunset sets at twelve o' clock."
        result = alphabet_position(text=test_string)
        self.assertEqual(result, "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")

    def test2(self):
        test_string = "'012 * bb*-"
        result = alphabet_position(text=test_string)
        self.assertEqual(result, "2 2")


if __name__ == "__main__":
    unittest.main()
