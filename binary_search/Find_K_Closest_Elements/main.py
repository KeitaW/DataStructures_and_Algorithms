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
        counter = 1
        while left >= 0 and right <= len(arr) - 1 and counter < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                closests.insert(0, arr[left])
                left -= 1
            else:
                closests.append(arr[right])
                right += 1
            counter += 1
        while left >= 0 and counter < k:
            closests.insert(0, arr[left])
            left -= 1
            counter += 1
        while right <= len(arr) - 1 and counter < k:
            closests.append(arr[right])
            right += 1
            counter += 1
        return closests


def find_closest(arr: List[int], x: int):
    def binary_search(left, right):
        # Find the left most element
        if left == right:
            return left
        pivot = (left + right) // 2
        if arr[pivot] < x:
            return binary_search(pivot + 1, right)
        else:
            return binary_search(left, pivot)
    return binary_search(0, len(arr) - 1)
