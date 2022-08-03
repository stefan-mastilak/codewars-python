# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
They would like your help with an application form that will tell prospective members
which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
Input will consist of a list of pairs. Each pair contains information for a single potential member.
Information consists of an integer for the person's age and an integer for the person's handicap.
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating
whether the respective member is to be placed in the senior or open category.

Example:
--------
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

"""

import unittest


def categorize(members: list):
    """
    Function will categorize players according to their age and handicap in croquet
    :param members: list of players profile info ([age, handicap])
    :return: players categories
    :rtype: list
    """
    result = []
    for age, handicap in members:
        result.append("Senior" if age >= 55 and handicap > 7 else "Open")
    return result


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
        result = categorize(members=test_input)
        self.assertEqual(result, ["Open", "Open", "Senior", "Open", "Open", "Senior"])


if __name__ == "__main__":
    unittest.main()
