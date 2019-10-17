from typing import List


def merge_sort_bottom_up(nums: List[int]) -> List[int]:
    """Merge sort algorithm(bottom up)

    Parameters
    ----------
    nums : List[int]
        array to be sorted

    Returns
    -------
    List[int]
        sorted array
    """
    # No need to sort
    if len(nums) <= 1:
        return nums

    pivot = len(nums) // 2
    left = merge_sort_bottom_up(nums[0:pivot])
    right = merge_sort_bottom_up(nums[pivot:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted list

    Parameters
    ----------
    left : List[int]
        The first list
    right : List[int]
        The second list

    Returns
    -------
    List[int]
        Merged list

    Notes
    --------
        The complexity of this function is O(N) 
    """
    left_cursor = right_cursor = 0
    merged = []
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor]:
            merged.append(left[left_cursor])
            left_cursor += 1
        else:
            merged.append(right[right_cursor])
            right_cursor += 1
    merged.append(left[left_cursor:])
    merged.append(right[right_cursor:])
    return merged
