# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self, level=0, right=False):
        return (
            "    " * (level - 1)
            + (" └──" if right else (
                " ├──" if level != 0 else ""))
            + " " + str(self.val) + "\n"
            + (self.left.__str__(level + 1, False) if self.left else "")
            + (self.right.__str__(level + 1, True) if self.right else "")
        )


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        .
        └── eua
            ├── tauh
            └── tuha
        """
        def r_serialize(node, string):
            if node is None:
                string += "None,"
            else:
                string += str(node.val) + ","
                string = r_serialize(node.left, string)
                string = r_serialize(node.right, string)
            return string
        return r_serialize(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # import ipdb
        # ipdb.set_trace()

        def r_deserialize(node=None):
            if data[0] == "None":
                data.pop(0)
                return None
            node = TreeNode(int(data.pop(0)))
            node.left = r_deserialize(data)
            node.right = r_deserialize(data)
            return node
        data = data.split(",")
        root = r_deserialize()
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
