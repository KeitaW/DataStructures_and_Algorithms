from typing import Generator
from itertools import starmap, zip_longest
# Definition for a binary tree node.


class TreeNode:
    pass


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def traverse(self) -> Generator[TreeNode, None, None]:
        def func(node: TreeNode):
            if node is None:
                return
            yield node
            yield from func(node.left)
            yield from func(node.right)

        return func(self)

    def __eq__(self, other):
        def eq_node(node1, node2):
            return node1.val == node2.val
        return all(starmap(eq_node, zip_longest(self.traverse(), other.traverse())))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, upper=float("inf"), lower=float("-inf")):
            if node is None:
                return True
            if node.val >= upper or node.val <= lower:
                return False
            return (validate(node.left, upper=node.val, lower=lower) and
                    validate(node.right, upper=upper, lower=node.val))
        return validate(root)
