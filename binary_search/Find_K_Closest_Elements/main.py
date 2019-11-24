from typing import List, Callable


class Solution:
    def findClosestElements(self, arr, k, x):
        ok = 0
        ng = len(arr) - k
        ok = binary_search_meguru(
            lambda mid: x - arr[mid] >= arr[mid + k] - x, ok, ng)
        print("ok, ", ok)
        while ok >= 1 and x - arr[ok] == arr[ok + k - 1] - x:
            ok -= 1
        return arr[ok: ok + k]

    def afindClosestElements(self, arr, k, x):
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
    edge = ok
    while abs(ok - ng) > 1:
        mid = ok + (ng - ok) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok if ok != edge else -1
