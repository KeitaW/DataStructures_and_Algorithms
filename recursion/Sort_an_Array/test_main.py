from recursion.Sort_an_Array.main import Solution


def test_main():
    solution = Solution()
    # test merge
    assert solution.merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert solution.sortArray([1, 5, 3]) == [1, 3, 5]
