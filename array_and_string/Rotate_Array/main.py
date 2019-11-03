from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """ Given an array, rotate the array to the right by k steps, where k is non-negative
        Do not return anything, modify nums in-place instead.

        Parameters
        ----------
        nums : List[int]
        k : int

        Returns
        -------
        None
        """

        def inplace_slice_reverse(start, end):
            while start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1

        nums.reverse()
        pivot = k % len(nums)
        inplace_slice_reverse(0, pivot-1)
        inplace_slice_reverse(pivot, len(nums)-1)
