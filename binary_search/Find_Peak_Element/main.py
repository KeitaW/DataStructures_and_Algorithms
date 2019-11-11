class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(left, right):
            if left == right:
                return left
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return binary_search(left, pivot)
            else:
                return binary_search(pivot + 1, right)
        return binary_search(0, len(nums) - 1)
