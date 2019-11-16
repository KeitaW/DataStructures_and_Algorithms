"""Ref
https://twitter.com/meguru_comp/status/697008509376835584
https://qiita.com/drken/items/97e37dd6143e33a64c8c
"""
from typing import List, Callable, Union


def binary_search_meguru(f: Callable[[int], bool], left: int, right: int) -> int:
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
    def search(left, right):
        mid = (left + right) // 2
        return (
            right if right - left <= 1 else
            search(left, mid) if f(mid) else
            search(mid, right)
        )
    return search(left, right)


def binary_search_meguru_iter(f: Callable[[int], bool], left: int, right: int) -> int:
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
    while right - left > 1:
        print(left, right)
        mid = (left + right) // 2
        if f(mid):
            right = mid
        else:
            left = mid
    return right


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
    left, right = -1, len(arr)
    return binary_search_meguru(lambda x: arr[x] >= target, left, right)


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
    left, right = -1, len(arr)
    return binary_search_meguru(lambda x: arr[x] >= target, left, right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
