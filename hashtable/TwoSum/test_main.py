from hashtable.TwoSum.main import Solution


def test_main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    assert solution.twoSum(nums, target) == [0, 1]
