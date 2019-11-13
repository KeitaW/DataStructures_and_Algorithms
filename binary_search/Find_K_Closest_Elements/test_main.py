from binary_search.Find_K_Closest_Elements.main import Solution, find_closest


def test_find_closest():
    assert find_closest([1, 2, 3, 4], 1) == 0
    assert find_closest([1, 2, 3, 4], 2) == 1
    assert find_closest([1, 2, 3, 4], 3) == 2
    assert find_closest([1, 2, 3, 4], 4) == 3
    assert find_closest([2, 4, 6], 2) == 0
    assert find_closest([2, 4, 6], 4) == 1
    assert find_closest([2, 4, 6], 6) == 2
    assert find_closest([2, 4, 6], 1) == 0
    assert find_closest([2, 4, 6], 3) == 0
    assert find_closest([2, 4, 6], 2) == 0
    assert find_closest([2, 2, 2], 2) == 0


def test_main():
    solution = Solution()
    assert solution.findClosestElements(
        [1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
    assert solution.findClosestElements(
        [1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]
