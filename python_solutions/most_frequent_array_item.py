# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
Complete the function to find the count of the most frequent item of an array.
You can assume that input is an array of integers.
For an empty array return 0

Example:
--------
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
output: 5 (because -1 is the most frequent item of the given array, and it occurs 5 times)

"""

import unittest


def most_frequent_item(inp: list):
    """
    Function to find the count of the most frequent item of an array.
    :param inp: input list
    :return: count of the most frequent item of given array
    :rtype: int
    """
    return max([inp.count(i) for i in set(inp)]) if inp else False


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_input = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
        result = most_frequent_item(inp=test_input)
        self.assertEqual(result, 5)

    def test2(self):
        test_input = [4, 0, 0, -1, 12, 3, -1, 3, 0, 2, 0, 9, 2]
        result = most_frequent_item(inp=test_input)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
