from typing import Callable


def binary_search_meguru(f: Callable[[int], bool], ok: int, ng: int) -> int:
    """General purpose binary search algorithm
    Parameters
    ----------
    f : Callable[[int], int]
        Monotonically increasing function
    left : int
        The left initial value that satisfies f(x) == True
    right : int
        The right initial value that satisfies f(x) == False
    Returns
    -------
    int
        The minimum x that satisfies f(x) = True
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
        print(ok, ng)
    return ok


class Solution:
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]

        def condition(idx):
            return nums[idx] - nums[0] < 0

        ng, ok = -1, len(nums)
        return nums[binary_search_meguru(condition, ok, ng)]

    def findMin1(self, nums):
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
