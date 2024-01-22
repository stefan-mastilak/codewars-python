"""

Task definition:
----------------
Write an algorithm that takes an array and moves all the zeros to the end, preserving the order of the other elements.

Example:
--------
move_zeros([1, 0, 1, 2, 0, 1, 3]) >> returns [1, 1, 2, 1, 3, 0, 0]

"""
import unittest


def move_zeros(array: list):
    return [x for x in array if x] + [0]*array.count(0)


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        self.assertEqual(move_zeros(
            array=[1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])

    def test2(self):
        self.assertEqual(move_zeros(
            array=[0, 0]),
            [0, 0])

    def test3(self):
        self.assertEqual(move_zeros(array=[0]),
                         [0])

    def test4(self):
        self.assertEqual(move_zeros(
            array=[9, 0, 9, 1, 2, 0, 1, 0, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
