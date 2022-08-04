# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.

Example:
--------
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""

import unittest


def reverser(text: str):
    """
    Function that accepts a string parameter, and reverses each word in the string
    :param text: text to be reversed
    :return: reversed text
    :rtype: str
    """
    return ' '.join(i[::-1] for i in text.split(' '))


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_input = "This is an example!"
        result = reverser(text=test_input)
        self.assertEqual(result, "sihT si na !elpmaxe")

    def test2(self):
        test_input = "double  spaces"
        result = reverser(text=test_input)
        self.assertEqual(result, "elbuod  secaps")

    def test3(self):
        test_input = " multiple    spaces   "
        result = reverser(text=test_input)
        self.assertEqual(result, " elpitlum    secaps   ")


if __name__ == '__main__':
    unittest.main()
