# REF: stefan.mastilak@gmail.com

"""

Task definition:
----------------
In this task you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

Example:
--------
alphabet_position("The sunset sets at twelve o' clock.")
Should return
"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
 ( as a string )

"""

import unittest
from string import ascii_lowercase


def get_position(text: str):
    """
    Function will return string with alphabet position of the letters in text
    :param text: input string
    :return: alphabet position of the letters in text
    :rtype: str
    """
    result = str()
    for i in text:
        if i.isalpha():
            result += f" {str(ascii_lowercase.index(i.lower()) + 1)}"
    return result.strip()


class TestSolution(unittest.TestCase):
    def test1(self):
        """
        Test solution
        """
        test_string = "The sunset sets at twelve o' clock."
        result = get_position(text=test_string)
        self.assertEqual(result, "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")


if __name__ == "__main__":
    unittest.main()