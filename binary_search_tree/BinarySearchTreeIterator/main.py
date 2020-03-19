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


class BSTIterator1:
    """BST Iterator by flattened BST list
    """

    def __init__(self, root: TreeNode):
        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []
        # Pointer to the next smallest element in the BST
        self.index = -1
        # Call to flatten the input binary search tree
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)


class BSTIterator2:
    """BST Iterator by controlled recursion
    """

    def __init__(self, root: TreeNode):
        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root: TreeNode):
        # For a given node, add all the elements in the leftmost
        # branch of the tree under it to the stack
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child,
        # all the helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
