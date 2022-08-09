# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
- It must start with a hashtag (#).
- All words must have their first letter capitalized.
- If the final result is longer than 40 chars it must return False.
- If the input or the result is an empty string it must return False.

Examples:
---------
" Hello there thanks for trying my Phrase"            =>  "#HelloThereThanksForTryingMyPhrase"
"    Hello     World   "                              =>  "#HelloWorld"
""                                                    =>  False
"This should return false because input is too long"  =>  False

"""

import unittest


def hashtag_generator(phrase: str):
    """
    Function for generating hashtag based on input phrase
    :param phrase: input text to be converted to hashtag
    :return: Hashtag word
    :rtype: str
    """
    tag = '#' + ''.join(i.capitalize() for i in phrase.split())
    return tag if phrase and len(tag) <= 40 else False


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_phrase = " Hello there thanks for trying my Phrase"
        result = hashtag_generator(phrase=test_phrase)
        self.assertEqual(result, "#HelloThereThanksForTryingMyPhrase")

    def test2(self):
        test_phrase = "    Hello     World   "
        result = hashtag_generator(phrase=test_phrase)
        self.assertEqual(result, "#HelloWorld")

    def test3(self):
        test_phrase = ""
        result = hashtag_generator(phrase=test_phrase)
        self.assertFalse(result)

    def test4(self):
        test_phrase = "This should return false because input is too long"
        result = hashtag_generator(phrase=test_phrase)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
