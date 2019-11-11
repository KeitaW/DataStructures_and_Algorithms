class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] <= nums[-1]:
            return nums[0]

        def binary_search(left, right):
            pivot = (left + right) // 2
            if nums[pivot + 1] < nums[pivot]:
                return nums[pivot + 1]
            if nums[pivot] >= nums[left]:
                return binary_search(pivot + 1, right)
            else:
                return binary_search(left, pivot - 1)
        return binary_search(0, len(nums) - 1)
