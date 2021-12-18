/**
* Solution in Javascript
* @param {number[]} nums
* @param {number} target
* @return {number}
*/
var search = function (nums, target) {
    let start = 0
    let end = nums.length - 1
    while (start <= end) {
        const pivot = parseInt((end - start) / 2) + start
        if (target === nums[pivot]) {
            return pivot
        } else if (target > nums[pivot]) {
            start = pivot + 1
        } else {
            end = pivot - 1
        }
    }
    return -1
};
