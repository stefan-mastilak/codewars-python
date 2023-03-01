"""
Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score a dice according to these rules.
You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single dice can only be counted once in each roll.
For example, a given "5" can only count as part of a triplet (contributing to the 500 points)
or as a single 50 points, but not both in the same roll.

Example scoring:

 dice       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

In some languages, it is possible to mutate the input to the function.
This is something that you should never do.
If you mutate the input, you will not be able to pass all the tests.
"""

import unittest


def dice_score(throw: list):
    """
    Evaluate dice throw and return score as an integer
    :param throw: list of five six-sided dice values (integers)
    :return: score as integer
    :rtype: int
    """
    triplets = {'111': 1000,
                '666': 600,
                '555': 500,
                '444': 400,
                '333': 300,
                '222': 200}
    singles = {'1': 100,
               '5': 50}
    score = 0
    throw.sort()
    throw = ''.join(map(str, throw))
    for k, v in triplets.items():
        if k in throw:
            score += v
            throw = throw.replace(k, '')
            break
    for i in throw:
        if i in singles.keys():
            score += singles[i]
    return score


class TestDiceSolution(unittest.TestCase):
    """
    Test dices game scoring solution
    """
    def test1(self):
        self.assertEqual(dice_score([5, 1, 3, 4, 1]), 250)

    def test2(self):
        self.assertEqual(dice_score([1, 1, 1, 3, 1]), 1100)

    def test3(self):
        self.assertEqual(dice_score([2, 3, 4, 6, 2]), 0)

    def test4(self):
        self.assertEqual(dice_score([4, 4, 4, 3, 3]), 400)

    def test5(self):
        self.assertEqual(dice_score([2, 4, 4, 5, 4]), 450)

    def test6(self):
        self.assertEqual(dice_score([1, 1, 5, 3, 3]), 250)

