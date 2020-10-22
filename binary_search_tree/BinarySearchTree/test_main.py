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
    assert bst.is_valid()


def test_iter(bst):
    bst_iter = iter(bst)
    assert next(bst_iter) == 3
    assert next(bst_iter) == 7
    assert next(bst_iter) == 9
    assert next(bst_iter) == 20


def test_delete(bst):
    bst.delete(3)
    bst_iter = iter(bst)
    assert next(bst_iter) == 7
    assert next(bst_iter) == 9
    assert next(bst_iter) == 20


def test_search(bst):
    assert bst.search(3).val == 3
    assert bst.search(-1) is None
