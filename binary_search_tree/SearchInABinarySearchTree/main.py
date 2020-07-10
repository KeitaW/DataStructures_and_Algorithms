class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, level=0, right=False):
        return (
            "    " * (level - 1)
            + (" └──" if right else (" ├──" if level != 0 else ""))
            + " "
            + str(self.val)
            + "\n"
            + (self.left.__str__(level + 1, False) if self.left else "")
            + (self.right.__str__(level + 1, True) if self.right else "")
        )


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def traverse(node: TreeNode):
            if (node is None) or (node.val == val):
                return node
            if node.val > val:
                return traverse(node.left)
            else:
                return traverse(node.right)

        return traverse(root)
