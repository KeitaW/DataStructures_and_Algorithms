class Node:
    def __init__(self, x, level=0):
        self.val = x
        self.left = None
        self.right = None
        self.level = level

    def __str__(self, last=True):
        # Those two values are used to backtrace the tree
        self.last = last
        arm = "" if self.level == 0 else (" └── " if last else " ├── ")
        # If the parent has succeeding child need spacing

        def get_spacing(node, spacing=""):
            if node.level == 0:
                return spacing
            spacing = ("     " if node.parent.last else " |   ") + spacing
            return get_spacing(node.parent, spacing)

        spacing = get_spacing(self)
        return (
            spacing
            + arm
            + str(self.val)
            + "\n"
            + "".join([
                self.left.__str__(
                    last=self.right is None) if self.left else "",
                self.right.__str__(last=True) if self.right else ""
            ])
        )

    def add_child(self, val):
        if self.left is None:
            self.left = Node(val, level=self.level + 1)
            self.left.parent = self
        elif self.right is None:
            self.right = Node(val, level=self.level + 1)
            self.right.parent = self
        else:
            assert "No space for the child"
