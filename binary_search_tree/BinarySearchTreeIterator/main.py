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


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        def traverse(node):
            if node.left:
                yield from traverse(node)
            yield node.val
            if node.right:
                yield from traverse(node)
        return traverse(self.root)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        pass


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
