"""Ref
https://twitter.com/meguru_comp/status/697008509376835584
https://qiita.com/drken/items/97e37dd6143e33a64c8c
"""
from typing import List, Callable, Union


# def binary_search_meguru(f: Callable[[int], bool], ok: int, ng: int) -> int:
#    """General purpose binary search algorithm
#
#    Parameters
#    ----------
#    f : Callable[[int], int]
#        Monotonically increasing function
#    left : int
#        The left initial value that satisfies f(x) == True
#    right : int
#        The right initial value that satisfies f(x) == False
#
#    Returns
#    -------
#    int
#        The minimum x that satisfies f(x) = True
#    """
#    def search(ok, ng):
#        mid = (ok + ng) // 2
#        return (
#            ok if abs(ok - ng) <= 1 else
#            search(mid, ng) if f(mid) else
#            search(ok, mid)
#        )
#    return search(ok, ng)


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
        print(ok, ng)
        mid = (ok + ng) // 2
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
    # なぜこれで良いか考える
    ng, ok = -1, len(arr)
    return binary_search_meguru(lambda x: arr[x] >= target, ok, ng)


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
        index of the minimum element. -1 if all the elements are less than target
    """
    # なぜこれで良いか考える
    ng, ok = len(arr), -1
    return binary_search_meguru(lambda x: arr[x] <= target, ok, ng)


def find_leftmost(arr: List[int], target: int) -> int:
    lb = lower_bound(arr, target)
    return lb if arr[lb] == target else -1


def find_rightmost(arr: List[int], target: int) -> int:
    ub = upper_bound(arr, target)
    return ub if arr[ub] == target else -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {1}, lower bound: {lower_bound(arr, 1)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {1}, upper bound: {upper_bound(arr, 1)}")

    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, find leftmost: {find_leftmost(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, find rightmost: {find_rightmost(arr, 2)}")
