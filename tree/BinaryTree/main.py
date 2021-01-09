class Node:
    def __init__(self, x, level=0, last=True):
        self.val = x
        self.left = None
        self.right = None
        self.level = level
        self.last = last

    def __str__(self):
        # Those two values are used to backtrace the tree
        arm = "" if self.level == 0 else (" └── " if self.last else " ├── ")
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
                self.left.__str__() if self.left else "",
                self.right.__str__() if self.right else ""
            ])
        )

    def add_child(self, val):
        if self.left is None:
            self.left = Node(val, level=self.level + 1, last=True)
            self.left.parent = self
        elif self.right is None:
            self.right = Node(val, level=self.level + 1, last=True)
            self.left.last = False
            self.right.parent = self
        else:
            assert "No space for the child"
