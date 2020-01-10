class Solution:
    def CountABC(self, s: str):
        if len(s) < 3:
            return 0
        count = 0
        for idx in range(len(s)):
            if s[idx : idx + 3] == "ABC":
                count += 1
        return count


if __name__ == "__main__":
    n, s = int(input()), input()
    solution = Solution()
    print(solution.CountABC(s))

