# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
Given an array of strings and a character to be used as border,
output the frame with the content inside.

Notes:
Always keep a space between the input string and the left and right borders.
The biggest string inside the array should always fit in the frame.
The input array is never empty.

Example:
--------
input: frame(['Create', 'a', 'frame'], '+')

Output:
++++++++++
+ Create +
+ a      +
+ frame  +
++++++++++

"""

import unittest


def frame(words: list, delim: str):
    """
    Function that will create frame around the given list of words.
    NOTE: The biggest string inside the array should always fit in the frame.
    :param words: list of words to be framed
    :param delim: border delimiter character
    :return: framed words
    :rtype: str
    """
    max_word = max(words, key=len)
    max_width = len(max_word) + 2 + 2 * len(delim)
    header = ''.join(delim * max_width)[:max_width]
    result = [f"{delim} {i} {delim}" if i == max_word
              else f"{delim} {i} " + " " * (len(max_word) - len(i)) + delim
              for i in words]
    result.insert(0, header)
    result.append(header)

    return f'\n'.join(i for i in result)


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        result = frame(words=['Create', 'a', 'frame'], delim='*')
        self.assertEqual(result, "**********\n"
                                 "* Create *\n"
                                 "* a      *\n"
                                 "* frame  *\n"
                                 "**********")

    def test2(self):
        result = frame(words=['Create', 'another', 'frame'], delim='****')
        self.assertEqual(result, "*****************\n"
                                 "**** Create  ****\n"
                                 "**** another ****\n"
                                 "**** frame   ****\n"
                                 "*****************")


if __name__ == "__main__":
    unittest.main()
