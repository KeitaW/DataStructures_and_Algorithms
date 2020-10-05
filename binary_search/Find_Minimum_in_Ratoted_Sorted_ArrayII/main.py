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
    return ok


class Solution:
    def findMin(self, nums):
        def condition(idx):
            return nums[idx] - nums[0] < 0

        ng, ok = 0, len(nums) - 1
        while nums[ng] == nums[ok] and ok >= 0:
            ok -= 1
        # In case the array is already sorted
        if nums[ng] < nums[ok]:
            return nums[ng]

        return nums[binary_search_meguru(condition, ok, ng)]
