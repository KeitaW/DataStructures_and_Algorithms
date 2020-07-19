from binary_search_tree.InsertIntoABST.main import TreeNode, Solution


def test_main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    solution = Solution()
    root = solution.insertIntoBST(root, val=5)
    assert root.right.left.val == 5

