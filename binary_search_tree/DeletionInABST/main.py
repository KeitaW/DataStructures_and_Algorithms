class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if (root.left is None) and (root.right is None):
                root = None
            # the node is not a leaf and has a right child
            elif root.right is not None:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

