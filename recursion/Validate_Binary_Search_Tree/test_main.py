from recursion.Validate_Binary_Search_Tree.main import TreeNode, Solution
from tree.binary_tree.Serialize_and_Deserialize_Binary_Tree.main import Codec


def test_tree_node():
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)

    cursor = root1.traverse()
    assert next(cursor).val == 2
    assert next(cursor).val == 1
    assert next(cursor).val == 3

    assert root1 == root2

    root2.left.left = TreeNode(9)
    assert root1 != root2


def test_main():
    codec = Codec()
    solution = Solution()
    """
         2
        / \
        1   3
    """
    assert solution.isValidBST(codec.deserialize(
        "2,1,None,None,3,None,None")) == True
    """
        5
        / \
        1   4
            / \
            3   6
    """
    tree = codec.deserialize(
        "5,1,None,None,4,None,None,3,None,None,6,None,None")
    assert solution.isValidBST(
        codec.deserialize("5,1,None,None,4,None,None,3,None,None,6,None,None")) == False
