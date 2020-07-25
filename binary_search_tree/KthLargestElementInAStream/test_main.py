from binary_search_tree.KthLargestElementInAStream.main import KthLargest

import numpy as np


def test_main():
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

    k = 1
    nums = []
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-2) == -2
    assert kthLargest.add(-4) == -2
    assert kthLargest.add(0) == 0
    assert kthLargest.add(4) == 4

    k = 1
    nums = np.arange(10)
    kthLargest = KthLargest(k, nums)
    import pdb
    pdb.set_trace()

