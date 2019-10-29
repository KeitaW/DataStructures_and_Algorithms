from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int], idx: int = 0, accumulator: int = 0) -> int:
        nums.sort()
        accumulator = 0
        for idx in range(0, len(nums), 2):
            accumulator += min(nums[idx], nums[idx+1])
        return accumulator
