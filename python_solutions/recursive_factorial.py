# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
Write functon to calculate factorial of a given number
Note that factorial of 0 and 1 is still 1, and it could not be calculated for negative numbers

Example:
--------
input =  4
output = 24

input = -5
output = False

"""

import unittest


def factorial(n):
    """
    Function for recursive factorial calculation
    :param n: number
    :return: factorial of n
    """
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1) if n > 0 else False


class TestSolution(unittest.TestCase):
    def test1(self):
        number = 0
        result = factorial(number)
        self.assertTrue(result, 1)

    def test2(self):
        number = 1
        result = factorial(number)
        self.assertTrue(result, 1)

    def test3(self):
        number = 5
        result = factorial(number)
        self.assertTrue(result, 120)

    def test4(self):
        number = -5
        result = factorial(number)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
