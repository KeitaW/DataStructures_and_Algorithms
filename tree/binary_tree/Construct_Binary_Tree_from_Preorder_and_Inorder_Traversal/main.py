from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        in_id_table = {val: idx for idx, val in enumerate(inorder)}

        def func(in_left, in_right):
            if in_left > in_right:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            in_root = in_id_table[val]
            root.left = func(in_left, in_root - 1)
            root.right = func(in_root + 1, in_right)
            return root
        return func(0, len(inorder) - 1)
