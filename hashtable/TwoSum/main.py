from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Two Sum using Hash table
        
        Parameters
        ----------
        nums : List[int]
        target : int
        
        Returns
        -------
        List[int]
        """
        table = {num: i for i, num in enumerate(nums)}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in table and table[complement] != i:
                return sorted([i, table[complement]])

    def twoSum_naive(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return sorted([i, j])
