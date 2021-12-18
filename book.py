# Problem 1: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?
import unittest

# assume the input is ASCII string -> so we have the max unique character is 128

# # use Set structure
# def isUnique(str: str) -> bool:
#     if (len(str) > 128):
#         return False
#     uniqueSet = set()
#     for char in str:
#         if (char in uniqueSet):
#             return False
#         uniqueSet.add(char)
#     return True

# use an boolean array with item i'th in array is the index of character in alphabet 
def isUnique(str: str) -> bool:
    if (len(str) > 128):
        return False
    uniqueChar = []
    for char in str:
        if (uniqueChar[ord(char)]):
            return False
        uniqueChar[ord(char)] = True
    return True
    
class TestFunc(unittest.TestCase):
    def setUp(self):
        self.instance = isUnique
    def test_1(self):
        self.assertEqual(self.instance('hello'), False)
    def test_2(self):
        self.assertEqual(self.instance('a'), True)

TestFunc().setUp()
unittest.main()
