from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def sort(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

    def merge(self, left, right):
        """Merge two sorted arrays
        """
        left_cursor = right_cursor = 0
        merged = []
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] < right[right_cursor]:
                merged.append(left[left_cursor])
                left_cursor += 1
            else:
                merged.append(right[right_cursor])
                right_cursor += 1
        merged += left[left_cursor:]
        merged += right[right_cursor:]
        return merged

    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        pivot = len(nums) // 2
        nums[:pivot] = self.merge_sort(nums[:pivot])
        nums[pivot:] = self.merge_sort(nums[pivot:])
        return self.merge(nums[:pivot], nums[pivot:])
