# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def guess_num(left, right):
            mid = (left + right) // 2
            reply = guess(mid)
            # Mid == answer
            if reply == 0:
                return mid
            # Mid is higher than answer
            if reply == 1:
                return guess_num(mid + 1, right)
            if reply == -1:
                return guess_num(left, mid - 1)
        return guess_num(0, n)
