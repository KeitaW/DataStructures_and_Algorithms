from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Given an array of integers nums, this function returns the "pivot" index of this array.
        We define the pivot index as the index where the sum of
        the numbers to the left of the index is equal to the sum of
        the numbers to the right of the index.
        If no such index exists, return -1
        Parameters
        ----------
        nums : List[int]
            input

        Returns
        -------
        int
            The pivot index
        """
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
