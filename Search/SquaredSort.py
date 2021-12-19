# https://leetcode.com/problems/squares-of-a-sorted-array
def sortedSquares(nums):
    left, right = 0, len(nums) - 1
    pointer = right
    result = [-1] * len(nums)
    
    while (left <= right):
        if (abs(nums[left]) > abs(nums[right])):
            result[pointer] = nums[left] ** 2
            left += 1
        else:
            result[pointer] = nums[right] ** 2
            right -= 1
        pointer -= 1
    return result

result = sortedSquares([-4,-1,0,3,10])
print(result)