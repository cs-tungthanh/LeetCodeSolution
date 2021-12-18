# command python3 sample.test.py -v
import unittest

class Solution:
    def function(self, l):
        return (l+l)

class TestFunc(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
    def test_1(self):
        self.assertEqual(self.instance.function(2), 8)
    def test_2(self):
        self.assertEqual(self.instance.function(2), 8)

TestFunc().setUp()
unittest.main()