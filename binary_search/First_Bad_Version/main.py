# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1

        def binary_search(left, right):
            pivot = (left + right) // 2
            print(pivot)
            if isBadVersion(pivot) == False and isBadVersion(pivot + 1) == True:
                return pivot + 1
            if isBadVersion(pivot):
                return binary_search(left, pivot - 1)
            else:
                return binary_search(pivot + 1, right)
        return binary_search(1, n)
