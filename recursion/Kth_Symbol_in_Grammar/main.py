class Solution:
    def kthGrammer_slow(self, N: int, K: int) -> int:
        # This solution causes Time Limit Exceeded when N=30
        # Time complexity: O(2**N)
        # Space complexity: O(2**N)
        def replace(row: str):
            return ''.join(['01' if char == '0' else '10' for char in list(row)])
        row = "0"
        for _ in range(1, N):
            row = replace(row)
        return row[K-1]

    def kthGrammer(self, N: int, K: int) -> int:
