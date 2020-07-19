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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        def insert(node: TreeNode):
            if (node is None) or (node.val == val):
                return node
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    insert(node.left)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    insert(node.right)

        insert(root)
        return root
