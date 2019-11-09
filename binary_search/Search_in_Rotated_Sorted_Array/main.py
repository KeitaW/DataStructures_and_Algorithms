class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        def binary_search(left, right):
            pivot = (left + right) // 2
            if left > right:
                return -1
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                return binary_search(left, pivot - 1)
            else:
                return binary_search(pivot + 1, right)

        rotation_index = find_rotation_index(nums)
        left = binary_search(0, rotation_index - 1)
        if left == -1:
            right = binary_search(rotation_index, len(nums) - 1)
            return right
        else:
            return left


def find_rotation_index(nums):
    if nums[0] <= nums[-1]:
        return 0

    def binary_search(left, right):
        pivot = (left + right) // 2
        if nums[pivot + 1] < nums[pivot]:
            return pivot + 1
        if nums[left] <= nums[pivot]:
            # [left, pivot] is sorted =>
            # rotation index should be in the right half
            return binary_search(pivot + 1, right)
        else:
            return binary_search(left, pivot - 1)
    return binary_search(0, len(nums) - 1)
