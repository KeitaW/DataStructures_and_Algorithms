from hashtable.MinimumIndexSumofTwoLists.main import Solution


def test_main():
    solution = Solution()
    assert solution.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"],
    ) == ["Shogun"]
