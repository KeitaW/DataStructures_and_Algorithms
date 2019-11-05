from typing import List


class Solution:
    def search_iterI(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return - 1

    def search_recurI(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] > target:
                return binary_search(left, mid - 1)
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return mid
        return binary_search(0, len(nums)-1)
