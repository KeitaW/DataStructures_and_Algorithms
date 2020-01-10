class Solution:
    def YenCoins(self, K: int, X: int):
        return "Yes" if 500 * K >= X else "No"


if __name__ == "__main__":
    K, X = map(int, input().split())
    solution = Solution()
    print(solution.YenCoins(K, X))

