from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """A modified binary search algorithm.
    If there are multiple target elements in nums, the algorithm returns the left most element.

    Parameters
    ----------
    nums : List[int]
    target : int

    Returns
    -------
    int
        Index of the target value in nums. -1 if there is no target element.
    """
    def debug_binary_search(search):
        def wrapper(left, right):
            print(nums[left:(right+1)])
            return search(left, right)
        return wrapper

    @debug_binary_search
    def _binary_search(left: int, right: int):
        if left == right:
            return left if nums[left] == target else -1
        pivot = (left + right) // 2
        if nums[pivot] < target:
            return _binary_search(pivot + 1, right)
        else:
            return _binary_search(left, pivot)

    return _binary_search(0, len(nums) - 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("ans: ", binary_search(arr, 2))
    arr = [1, 2, 3, 4, 5, 5]
    print("ans: ", binary_search(arr, 5))
    arr = [1, 1, 1, 1, 1]
    print("ans: ", binary_search(arr, 1))
