# REF: stefan.mastilak@gmail.com

"""

Task definition:
-----------------
Write a function, which takes a non-negative integer (seconds) as input
and returns the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures.

Example:
--------------
input = 5
output = "00:00:05"

input = 62
output = "00:01:02"

"""

import unittest


def human_time_converter(seconds: int):
    """
    Function will convert seconds to human-readable time (HH:MM:SS)
    :param seconds: seconds as integer
    :return: human-readable time as string
    :rtype: str
    """
    return f"{(seconds//3600):02d}:{(seconds // 60 % 60):02d}:{(seconds % 60):02d}" if 0 <= seconds <= 359999 else False


class TestSolution(unittest.TestCase):
    """
    Test solution
    """
    def test1(self):
        test_input = 62
        result = human_time_converter(seconds=test_input)
        self.assertTrue(result, "00:01:02")

    def test2(self):
        test_input = 359999
        result = human_time_converter(seconds=test_input)
        self.assertTrue(result, "99:59:59")

    def test3(self):
        test_input = 360000
        result = human_time_converter(seconds=test_input)
        self.assertFalse(result)

    def test4(self):
        test_input = -360
        result = human_time_converter(seconds=test_input)
        self.assertFalse(result)

    def test5(self):
        test_input = 0
        result = human_time_converter(seconds=test_input)
        self.assertTrue(result, "00:00:00")


if __name__ == "__main__":
    unittest.main()
