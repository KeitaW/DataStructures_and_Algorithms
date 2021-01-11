from collections import Counter


class HuffmanNode:
    def __init__(self, char, level=0, last=True):
        self.char = char
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
            + str(self.char)
            + "\n"
            + "".join([
                self.left.__str__() if self.left else "",
                self.right.__str__() if self.right else ""
            ])
        )

    def add_child(self, char):
        if self.left is None:
            self.left = HuffmanNode(char, level=self.level + 1, last=True)
            self.left.parent = self
        elif self.right is None:
            self.right = HuffmanNode(char, level=self.level + 1, last=True)
            self.left.last = False
            self.right.parent = self
        else:
            assert "No space for the child"


class HuffmanCoding:
    def __init__(self) -> None:
        self.ordered_chars = None

    def encode(string: str) -> None:
        counter = Counter(string)
        n_unique_chars = len(counter.keys())
        sorted_chars = [
            char for char, count
            in counter.most_common(n_unique_chars)
        ]
        print(sorted_chars)

    def decode(string: str) -> str:
        pass
