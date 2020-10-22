from pytest import fixture

from binary_search_tree.BinarySearchTree.main import BinarySearchTree


@fixture
def bst():
    tree = BinarySearchTree()
    tree.insert(7)
    tree.insert(3)
    tree.insert(9)
    tree.insert(20)
    return tree


def test_validate(bst):
    import pdb

    pdb.set_trace()
    assert bst.is_valid()

