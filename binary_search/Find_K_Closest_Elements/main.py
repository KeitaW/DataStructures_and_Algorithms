from typing import List, Callable


class Solution:
    def findClosestElements(self, arr, k, x):
        if len(arr) <= 1:
            return arr
        return find_k_closest(arr, x, k)

    def findClosestElements_alt(self, arr, k, x):
        ok = 0
        ng = len(arr) - k

        while abs(ok - ng) > 1:
            mid = ok + (ng - ok) // 2
            if x - arr[mid] >= arr[mid + k] - x:
                ok = mid
            else:
                ng = mid

        while ok >= 1 and x - arr[ok] == arr[ok + k - 1] - x:
            ok -= 1
        return arr[ok: ok + k]


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


def lower_bound(arr: List[int], target: int) -> int:
    """Find the mimimun/leftmost element x in arr that satisfies x >= target 

    Parameters
    ----------
    arr : List[int]
        sorted array
    target : int

    Returns
    -------
    int
        index of the minimum element. -1 if all the elements are less than target
    """
    ng, ok = -1, len(arr)
    ok = binary_search_meguru(lambda x: arr[x] >= target, ok, ng)
    return ok if ok != len(arr) else -1


def upper_bound(arr: List[int], target: int) -> int:
    """Find the maximum/rightmost element x in arr that satisfies x <= target 

    Parameters
    ----------
    arr : List[int]
        sorted array
    target : int

    Returns
    -------
    int
        index of the minimum element. -1 if all the elements are more than target
    """
    ng, ok = len(arr), -1
    ok = binary_search_meguru(lambda x: arr[x] <= target, ok, ng)
    return ok if ok != -1 else -1


def find_closest(arr: List[int], target: int) -> int:
    ub = upper_bound(arr, target)
    lb = lower_bound(arr, target)
    return ub if abs(arr[ub] - target) <= abs(arr[lb] - target) else lb


def find_k_closest(arr: List[int], target: int, k: int) -> int:
    left = find_closest(arr, target)
    right = left

    def next_lr(left, right):
        next_left = max(0, left - 1)
        next_right = min(right + 1, len(arr) - 1)
        if right == next_right:
            return (next_left, right)
        if left == next_left:
            return (left, next_right)
        if abs(arr[next_left] - target) <= abs(arr[next_right] - target):
            return (next_left, right)
        else:
            return (left, next_right)

    for _ in range(k-1):
        left, right = next_lr(left, right)
    return arr[left:(right+1)]
