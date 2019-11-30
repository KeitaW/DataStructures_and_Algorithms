class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, upper=float("inf"), lower=float("-inf")):
            if node is None:
                return True
            if node.val >= upper or node.val <= lower:
                return False
            return (
                validate(node.left, upper=node.val, lower=lower) and
                validate(node.right, upper=upper, lower=node.val)
            )
        return validate(root)
