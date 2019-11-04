from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cursor = len(nums) - 1
        idx = 0
        while True:
            if nums[idx] == 0:
                elem = nums.pop(idx)
                nums.append(elem)
                cursor -= 1
            else:
                idx += 1
            if idx >= cursor:
                return
