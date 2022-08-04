# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!
Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples:
---------
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

import unittest


def hashtag_generator(phrase: str):
    """
    Function for generating hashtag based on input phrase
    :param phrase: input text to be converted to hashtag
    :return: Hashtag word
    :rtype: str
    """
    return '#' + ''.join(i.capitalize() for i in phrase.split()) if phrase else False


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_phrase = " Hello there thanks for trying my Kata"
        result = hashtag_generator(phrase=test_phrase)
        self.assertEqual(result, "#HelloThereThanksForTryingMyKata")

    def test2(self):
        test_phrase = "    Hello     World   "
        result = hashtag_generator(phrase=test_phrase)
        self.assertEqual(result, "#HelloWorld")

    def test3(self):
        test_phrase = ""
        result = hashtag_generator(phrase=test_phrase)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
