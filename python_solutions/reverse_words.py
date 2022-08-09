# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
Complete the function that accepts a string parameter, and reverses each word in the string.
- All spaces in the string should be retained.
- Return False if empty string passed in

Example:
--------
"This is an example!" ==> "sihT si na !elpmaxe"
"Double  spaces"      ==> "elbuoD  secaps"
""                    ==> False

"""

import unittest


def reverser(text: str):
    """
    Function that accepts a string parameter, and reverses each word in the string
    :param text: text to be reversed
    :return: reversed text
    :rtype: str
    """
    return ' '.join(i[::-1] for i in text.split(' ')) if text else False


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_input = "This is an example!"
        result = reverser(text=test_input)
        self.assertEqual(result, "sihT si na !elpmaxe")

    def test2(self):
        test_input = "Double  spaces"
        result = reverser(text=test_input)
        self.assertEqual(result, "elbuoD  secaps")

    def test3(self):
        test_input = " multiple    spaces   "
        result = reverser(text=test_input)
        self.assertEqual(result, " elpitlum    secaps   ")

    def test4(self):
        test_input = ""
        result = reverser(text=test_input)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
