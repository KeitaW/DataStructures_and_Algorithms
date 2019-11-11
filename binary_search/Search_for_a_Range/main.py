class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(left, right):
            if left > right:
                return -1
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                return binary_search(pivot + 1, right)
            else:
                return binary_search(left, pivot - 1)

        target_idx = binary_search(0, len(nums)-1)

        def find_range(target_idx):
            if target_idx == -1:
                return [-1, -1]
            left, right = target_idx, target_idx
            while left >= 0 and nums[left] == target:
                left -= 1
            while right <= len(nums) - 1 and nums[right] == target:
                right += 1
            return [left + 1, right - 1]
        return find_range(target_idx)
