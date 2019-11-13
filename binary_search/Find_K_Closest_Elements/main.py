from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ Given a sorted array, two integers k and x, find the k closest elements to x in the array.
        The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

        Parameters
        ----------
        arr : List[int]
        k : int
        x : int

        Returns
        -------
        List[int]
        """
        closest_idx = find_closest(arr, x)
        left, right = closest_idx - 1, closest_idx + 1
        closests = [arr[closest_idx]]
        counter = 0
        print(closests)
        while left >= 0 and right <= len(arr) - 1:
            if abs(arr[left] - x) < abs(arr[right] - x):
                closests.insert(0, arr[left])
                left -= 1
            else:
                closests.insert(-1, arr[right])
                right += 1
            counter += 1
        print(closests)
        while left >= 0 and counter <= k:
            closests.insert(0, arr[left])
            left -= 1
            counter += 1
        while right <= len(arr) - 1 and counter <= k:
            closests.insert(-1, arr[right])
            right += 1
            counter += 1
        return closests


def find_closest(arr: List[int], x: int):

    def binary_search(left, right):
        pivot = (left + right) // 2
        print(left, right)
        if left == right:
            return left
        if arr[pivot] == x:
            return pivot
        if abs(arr[pivot] - x) >= abs(arr[pivot + 1] - x):
            return binary_search(pivot + 1, right)
        else:
            return binary_search(left, pivot - 1)

    closest = binary_search(0, len(arr) - 1)
    # Find the left most element
    left = closest
    while left >= 1 and abs(arr[left-1]-x) == abs(arr[closest]-x):
        left -= 1
    return left
