class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return bin(K-1).count('1') % 2

    def kthGrammar_flip_variant(self, N: int, K: int) -> int:
        return 0 if N == 1 else (
            self.kthGrammar_flip_variant(N-1, K) if K <= (2**(N-2)) else(
                self.kthGrammar_flip_variant(N-1, K - 2**(N-2)) ^ 1
            )
        )

    def kthGrammar_recursive_parent_variant(self, N: int, K: int) -> int:
        return 0 if N == 1 else (1 - K % 2) ^ self.kthGrammar_recursive_parent_variant(N-1, (K+1)//2)

    def kthGrammar_slow(self, N: int, K: int) -> int:
        # This solution causes Time Limit Exceeded when N=30
        # Time complexity: O(2**N)
        # Space complexity: O(2**N)
        def replace(row: str):
            return ''.join(['01' if char == '0' else '10' for char in list(row)])
        row = "0"
        for _ in range(1, N):
            row = replace(row)
        return row[K-1]
