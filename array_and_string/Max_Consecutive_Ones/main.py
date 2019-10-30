from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_k = 0
        k = 0
        for i in range(len(nums)):
            k = k + 1 if nums[i] == 1 else 0
            max_k = k if k > max_k else max_k
        return max_k
