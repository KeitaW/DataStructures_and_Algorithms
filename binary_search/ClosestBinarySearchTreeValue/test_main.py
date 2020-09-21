from binary_search.ClosestBinarySearchTreeValue.main import TreeNode, Solution


def test_main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    solution = Solution()
    assert solution.closestValue(root, 3.714286) == 4
    root = TreeNode(1)
    assert solution.closestValue(root, 4.428571) == 1
    root = TreeNode(2)
    root.left = TreeNode(1)
    assert solution.closestValue(root, 2147483647.0) == 2
