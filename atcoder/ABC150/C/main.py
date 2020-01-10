from itertools import permutations


class Solution:
    def CountOrder(self, sequence1, sequence2):
        l = list(permutations(range(1, n + 1)))
        index1 = l.index(sequence1)
        index2 = l.index(sequence2)
        return abs(index1 - index2)


if __name__ == "__main__":
    n = int(input())
    sequence1 = tuple(map(int, input().split()))
    sequence2 = tuple(map(int, input().split()))
    solution = Solution()
    print(solution.CountOrder(sequence1, sequence2))

