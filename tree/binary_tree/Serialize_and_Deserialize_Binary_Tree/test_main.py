import pytest
from tree.binary_tree.Serialize_and_Deserialize_Binary_Tree.main import Codec, TreeNode


@pytest.fixture
def test_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    return root


@pytest.fixture
def test_sequence():
    return "1,2,None,None,3,4,None,None,5,None,None,"


def test_serialize(test_tree, test_sequence):
    codec = Codec()
    sequence = codec.serialize(test_tree)
    assert sequence == test_sequence


def test_deserialize(test_tree, test_sequence):
    codec = Codec()
    tree = codec.deserialize(test_sequence)
    assert tree == test_tree
