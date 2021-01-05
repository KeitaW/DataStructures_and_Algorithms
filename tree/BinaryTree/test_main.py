from tree.BinaryTree.main import Node


def test_node():
    root = Node(1)
    root.add_child(2)
    root.add_child(3)
    root.left.add_child(4)
    root.left.add_child(5)
    root.right.add_child(6)
    root.right.add_child(7)
    return root


if __name__ == "__main__":
    tree = test_node()
    print(tree)
