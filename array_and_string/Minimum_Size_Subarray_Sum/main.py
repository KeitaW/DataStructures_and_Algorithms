from typing import List
import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """Given an array of n positive integers and a positive integer s,
        find the minimal length of a contiguous subarray of which the sum ≥ s.
        If there isn't one, return 0 instead.

        Parameters
        ----------
        s : int
        nums : List[int]

        Returns
        -------
        int
        """
        ans = sys.maxsize
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= s:
                ans = min(ans, right + 1 - left)
                total -= nums[left]
                left += 1
        return ans if ans != sys.maxsize else 0
