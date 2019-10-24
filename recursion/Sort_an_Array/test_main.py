from recursion.Sort_an_Array.main import Solution


def test_main():
    solution = Solution()
    # test merge
    assert solution.merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert solution.sortArray([1, 5, 3]) == [1, 3, 5]
    assert solution.sortArray([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
