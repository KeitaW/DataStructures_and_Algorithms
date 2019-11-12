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
        closests = [find_closest(0, len(arr) - 1)]
        left, right = closests[0] - 1, closests[0] + 1
        for _ in range(k - 1):
            pass


def find_closest(arr: List[int], x: int):
    print("start")

    def binary_search(left, right):
        pivot = (left + right) // 2
        print(left, right)
        if left == right:
            return left
        if arr[pivot] == x:
            return pivot
        if abs(arr[left] - x) >= abs(arr[pivot] - x):
            return binary_search(pivot + 1, right)
        else:
            return binary_search(left, pivot - 1)

    closest = binary_search(0, len(arr) - 1)
    # Find the left most
    left = closest
    while abs(arr[left-1]-x) == abs(arr[closest]-x):
        left -= 1
    return left
