"""Ref
https://twitter.com/meguru_comp/status/697008509376835584
https://qiita.com/drken/items/97e37dd6143e33a64c8c
"""
from typing import List, Callable


def binary_search_meguru_recur(f: Callable[[int], bool], ok: int, ng: int) -> int:
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

    def search(ok, ng):
        mid = ok + (ng - ok) // 2
        return (
            ok if abs(ok - ng) <= 1 else
            search(mid, ng) if f(mid) else
            search(ok, mid)
        )
    ok = search(ok, ng)
    return ok if ok != edge else -1


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


def find_leftmost(arr: List[int], target: int) -> int:
    lb = lower_bound(arr, target)
    return lb if (lb == -1 or arr[lb] == target) else -1


def find_rightmost(arr: List[int], target: int) -> int:
    ub = upper_bound(arr, target)
    return ub if (ub == -1 or arr[ub] == target) else -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {100}, lower bound: {lower_bound(arr, 100)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, lower bound: {lower_bound(arr, 0)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, lower bound: {lower_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {1}, lower bound: {lower_bound(arr, 1)}")

    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {100}, upper bound: {upper_bound(arr, 100)}")
    arr = [1, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, upper bound: {upper_bound(arr, 0)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {2}, upper bound: {upper_bound(arr, 2)}")
    arr = [2, 2, 2]
    print(f"arr: {arr}, target: {1}, upper bound: {upper_bound(arr, 1)}")

    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, find leftmost: {find_leftmost(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, find leftmost: {find_leftmost(arr, 0)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {2}, find rightmost: {find_rightmost(arr, 2)}")
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(f"arr: {arr}, target: {0}, find rightmost: {find_rightmost(arr, 0)}")

    arr = [1, 2, 100, 101, 102]
    target = 99
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 100, 101, 102]
    target = 200
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 100, 101, 102]
    target = 10
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 100, 101, 102]
    target = -1
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [2, 2, 2]
    target = 2
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 2, 2]
    target = 2
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")
    arr = [1, 2, 2, 2, 4, 4, 4]
    target = 3
    print(f"arr: {arr}, target: {target}, closest: {find_closest(arr, target)}")

    arr = [1, 2, 100, 101, 102]
    target = 99
    k = 3
    print(
        f"arr: {arr}, target: {target}, k: {k}, k closest: {find_k_closest(arr, target, k)}")

    arr = [1, 2, 3, 4, 5]
    target = 3
    k = 4
    print(
        f"arr: {arr}, target: {target}, k: {k}, k closest: {find_k_closest(arr, target, k)}")

    arr = [1, 2]
    target = 1
    k = 1
    print(
        f"arr: {arr}, target: {target}, k: {k}, k closest: {find_k_closest(arr, target, k)}")

    arr = [1, 2, 3, 4, 5]
    target = -1
    k = 4
    print(
        f"arr: {arr}, target: {target}, k: {k}, k closest: {find_k_closest(arr, target, k)}")

    arr = [1, 2, 3, 4, 5]
    target = 3
    k = 4
    print(
        f"arr: {arr}, target: {target}, k: {k}, k closest: {find_k_closest(arr, target, k)}")

    arr = [0, 1, 2, 2, 2, 3, 6, 8, 8, 9]
    target = 9
    k = 5
    print(
        f"arr: {arr}, target: {target}, k: {k}, k closest: {find_k_closest(arr, target, k)}")
