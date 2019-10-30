from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Given an array nums and a value val, remove all instances of that value in-place and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.

        Parameters
        ----------
        nums : List[int]
        val : int

        Returns
        -------
        int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(f"New array: {nums}")
        return k
