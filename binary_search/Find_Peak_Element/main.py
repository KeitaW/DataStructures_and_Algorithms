from typing import Callable


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        idx = binary_search_meguru(
            lambda mid: nums[mid] < nums[mid+1], 0, len(nums)-1)
        return idx + 1


def binary_search_meguru(f: Callable[[int], bool], ok: int, ng: int) -> int:
    """General purpose binary search algorithm

    Parameters
    ----------
    f : Callable[[int], int]
    ok : int
    ng : int

    Returns
    -------
    int
    """
    while abs(ok - ng) > 1:
        mid = ok + (ng - ok) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok
