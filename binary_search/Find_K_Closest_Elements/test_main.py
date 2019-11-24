from binary_search.Find_K_Closest_Elements.main import Solution


# def test_find_closest():
#    assert find_closest([1, 2, 3, 4], 1) == 0
#    assert find_closest([1, 2, 3, 4], 2) == 1
#    assert find_closest([1, 2, 3, 4], 3) == 2
#    assert find_closest([1, 2, 3, 4], 4) == 3
#    assert find_closest([2, 4, 6], 2) == 0
#    assert find_closest([2, 4, 6], 4) == 1
#    assert find_closest([2, 4, 6], 6) == 2
#    assert find_closest([2, 4, 6], 1) == 0
#    assert find_closest([2, 4, 6], 3) == 0
#    assert find_closest([2, 4, 6], 2) == 0
#    assert find_closest([2, 2, 2], 2) == 0
#    import pudb
#    pudb.set_trace()
#    assert find_closest([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 5) == 6


def test_main():
    solution = Solution()
    assert solution.findClosestElements(
        [1, 2], k=1, x=1) == [1]
    assert solution.findClosestElements(
        [1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
    assert solution.findClosestElements(
        [1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]
    assert solution.findClosestElements(
        [1, 2, 2, 2, 5, 5, 5, 8, 9, 9], k=4, x=0) == [1, 2, 2, 2]
    import pudb
    pudb.set_trace()
    assert solution.findClosestElements(
        [0, 0, 1, 2, 3, 3, 4, 7, 7, 7, 8], k=3, x=5) == [3, 3, 4]
