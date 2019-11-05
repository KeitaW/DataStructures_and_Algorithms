class Solution:
    def mySqrt(self, x: int) -> int:
        def search(left, right):
            mid = (left + right) // 2
            if left > right:
                return left if right ** 2 > x else right
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                return search(left, mid - 1)
            elif mid**2 < x:
                return search(mid + 1, right)
        return search(0, x)
