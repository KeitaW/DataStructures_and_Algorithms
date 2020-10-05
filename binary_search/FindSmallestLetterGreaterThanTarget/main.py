from typing import List, Callable


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


def upper_bound(arr: List[int], target: int) -> int:
    """Find the maximum/rightmost element x in arr that satisfies x >= target 
    Parameters
    ----------
    arr : List[int]
        sorted array
    target : int
    Returns
    -------
    int
        index of the minimum element.
        -1 if all the elements are less than target
    """
    ng, ok = len(arr), -1
    return binary_search_meguru(lambda x: arr[x] <= target, ok, ng)


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ub = upper_bound(letters, target)
        if ub == len(letters) - 1:
            return letters[0]
        else:
            return letters[ub + 1]

