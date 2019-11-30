class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        output = []
        idx = [None]

        def func(node: TreeNode):
            if node is None:
                return
            if node.left:
                func(node.left)
            output.append(node)
            if node.val == p.val:
                idx[0] = len(output)
            if node.right:
                func(node.right)
        func(root)
        if idx[0] and idx[0] <= len(output) - 1:
            return output[idx[0]]
        else:
            return None
