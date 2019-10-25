from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1
        if len(nums) == 1 and nums[0] == 1:
            return 0
        largest = max(nums)
        largest_idx = nums.index(largest)
        nums.pop(largest_idx)
        second_largest = max(nums)
        if (largest // 2) >= second_largest:
            return largest_idx
        else:
            return -1

    def ans_dominantIndex(self, nums):
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1
