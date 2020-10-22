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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.root.__str__()

    def is_valid(self) -> bool:
        def validate(node, upper=float("inf"), lower=float("-inf")):
            if node is None:
                return True
            if node.val >= upper or node.val <= lower:
                return False
            return validate(node.left, node.val, lower) and validate(
                node.right, upper, node.val
            )

        return validate(self.root)

    def __leftmost_inorder(self, root: TreeNode):
        """
        For a given node, add all the elements in the leftmost
        branch of the tree under it to the stack

        Parameters
        ----------
        root : TreeNode
            [description]
        """
        while root:
            self.stack.append(root)
            root = root.left

    def __next__(self) -> int:
        """
        @return the next smallest number
        """

        def has_next() -> bool:
            return len(self.stack) > 0

        if not has_next():
            raise StopIteration()

        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child,
        # all the helper function for the right child
        if topmost_node.right:
            self.__leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def __iter__(self):
        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self.__leftmost_inorder(self.root)
        return self

    def insert(self, val: int):
        if self.root is None:
            self.root = TreeNode(val)

        def __insert(node: TreeNode):
            if (node is None) or (node.val == val):
                return node
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    __insert(node.left)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    __insert(node.right)

        __insert(self.root)

    def inorder(self, node: TreeNode):
        return (
            self.inorder(node.left) + [node.val] + self.inorder(node.right)
            if node
            else []
        )

    def successor(self, node: TreeNode):
        node = node.right
        while node.left is not None:
            node = node.left
        return node.val

    def predecessor(self, node: TreeNode):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def delete(self, key: int):
        if self.root is None:
            return None

        def __delete(node, key: int):
            # delete from the right subtree
            if key > node.val:
                node.right = __delete(node.right, key)
            # delete from the left subtree
            elif key < node.val:
                node.left = __delete(node.left, key)
            # delete the current node
            else:
                # the node is a leaf
                if (node.left is None) and (node.right is None):
                    node = None
                # the node is not a leaf and has a right child
                elif node.right is not None:
                    node.val = self.successor(node)
                    node.right = __delete(node.right, node.val)
                # the node is not a leaf, has no right child, and has a left child
                else:
                    node.val = self.predecessor(node)
                    node.left = __delete(node.left, node.val)

        __delete(self.root, key)

    def search(self, val: int) -> TreeNode:
        def traverse(node: TreeNode):
            if (node is None) or (node.val == val):
                return node
            if node.val > val:
                return traverse(node.left)
            else:
                return traverse(node.right)

        return traverse(self.root)
