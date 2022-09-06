# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
The company you work for has just been awarded a contract to build a payment gateway.
In order to help move things along, you have volunteered to create a function that will take a
float and return the amount formatting in dollars and cents.

39.99 becomes $39.99

The rest of your team will make sure that the argument is sanitized before being passed to your
function, although you will need to account for adding trailing zeros if they are missing
(though you won't have to worry about a dangling period).

Example:
--------
3 needs to become $3.00
3.1 needs to become $3.10
7.126 needs to become $7.13

"""
import unittest


def price_converter(price: float):
    """
    Function that will take a float and return the amount formatting in dollars and cents.
    :param price: price to be converted
    :return: converted price
    :rtype: str
    """
    price = round(float(price), 2)
    return '$' + str(price) if len(str(price).split('.')[-1]) > 1 else '$' + str(price) + '0'


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_input = 4
        result = price_converter(price=test_input)
        self.assertEqual(result, '$4.00')

    def test2(self):
        test_input = 0.5
        result = price_converter(price=test_input)
        self.assertEqual(result, '$0.50')

    def test3(self):
        test_input = 0
        result = price_converter(price=test_input)
        self.assertEqual(result, '$0.00')

    def test4(self):
        test_input = 7.126
        result = price_converter(price=test_input)
        self.assertEqual(result, '$7.13')

    def test5(self):
        test_input = 25.102
        result = price_converter(price=test_input)
        self.assertEqual(result, '$25.10')


if __name__ == '__main__':
    unittest.main()
