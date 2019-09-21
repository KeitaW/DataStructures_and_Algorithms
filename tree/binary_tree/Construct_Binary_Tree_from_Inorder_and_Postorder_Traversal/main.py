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
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            in_root = inorder_node_table[val]
            root.right = func(in_root + 1, in_right)
            root.left = func(in_left, in_root - 1)
            return root

        inorder_node_table = {
            val: idx for idx, val in enumerate(inorder)}
        return func(0, len(inorder) - 1)
