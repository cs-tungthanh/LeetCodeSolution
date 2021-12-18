def search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while (start <= end):
        mid = int((end - start) / 2) + start
        if (target == nums[mid]):
            return mid
        elif (target > nums[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return -1

# https://leetcode.com/problems/search-insert-position/
def searchInsert(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    if (target > nums[end]):
        return end + 1
    while start <= end:
        middle = int(start + (end - start)/2)
        if nums[middle] == target:
            return nums.index(nums[middle])
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return start
