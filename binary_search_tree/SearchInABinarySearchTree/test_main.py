from binary_search_tree.SearchInABinarySearchTree.main import TreeNode, Solution


def test_main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    solution = Solution()
    node = solution.searchBST(root, val=2)
    assert node.val == 2
    assert node.left.val == 1
    assert node.right.val == 3

