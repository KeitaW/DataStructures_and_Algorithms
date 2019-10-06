from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def func(in_left, in_right):
            if in_left >= in_right:
                return
            root = TreeNode(postorder[in_right])
            in_root = inorder_node_table[root.val]
            root.left = func(in_left, in_root - 1)
            root.right = func(in_root + 1, in_right)
            return root
        inorder_node_table = {idx: val for idx, val in enumerate(inorder)}
        return func(0, len(inorder) - 1)


if __name__ == "__main__":
    solution = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    solution.buildTree(inorder, postorder)
