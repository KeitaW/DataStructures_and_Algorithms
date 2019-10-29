from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int], idx: int = 0, accumulator: int = 0) -> int:
        return self.arrayPairSum(
            nums, idx+1, accumulator + min(nums[idx], nums[idx+(len(nums)//2)])
        ) if idx < (len(nums) // 2) else accumulator

    def arrayPairSum(self, nums: List[int], idx: int = 0, accumulator: int = 0) -> int:
        pivot = len(nums) // 2
