from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        prev_elem = nums[0]
        idx = 1
        while True:
            if nums[idx] == prev_elem:
                nums.pop(idx)
            else:
                prev_elem = nums[idx]
                idx += 1
            if idx >= len(nums):
                break
        return len(nums)
