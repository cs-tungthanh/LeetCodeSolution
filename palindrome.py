import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) < 2):
            return s
        max_length = 1
        max_str = s[0]
        value = ''
        for (idx, letter) in enumerate(s):
            value += letter
            j = idx + 1
            while j < len(s):
                value += s[j]
                length_value = len(value)
                if (length_value >= max_length):
                    mid_idx = int(length_value / 2)
                    if (length_value % 2 == 0):
                        start_second_idx = mid_idx
                    elif (((length_value -1) % 2) == 0):
                        start_second_idx = mid_idx + 1
                    if ((value[:mid_idx] == value[start_second_idx:][::-1])):
                        max_str = value
                        max_length = length_value
                j += 1
            value = ''
        return max_str


class TestFunc(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
    def test_1(self):
        self.assertEqual(self.instance.longestPalindrome("babad"), "aba")
    def test_2(self):
        self.assertEqual(self.instance.longestPalindrome("cbbd"), "bb")
    def test_3(self):
        self.assertEqual(self.instance.longestPalindrome("a"), "a")
    def test_4(self):
        self.assertEqual(self.instance.longestPalindrome("ac"), "a")
    def test_5(self):
        self.assertEqual(self.instance.longestPalindrome("aacabdkacaa"), "aca")

TestFunc().setUp()
unittest.main()