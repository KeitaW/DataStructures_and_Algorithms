import pytest
from tree.binary_tree.Lowest_Common_Ancestor_of_a_Binary_Tree.main import Solution, TreeNode


@pytest.fixture
def test_tree():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    return root


def find_node_by_name(root: TreeNode, val: str) -> TreeNode:
    """Do level order traversal and find a node by name.
    """
    if root.val == val:
        return root
    current = [root]
    while current:
        next_level = []
        for node in current:
            if node.val == val:
                return node
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
    assert AttributeError, "Not Found"


def test_find_node_by_name(test_tree):
    assert find_node_by_name(test_tree, 1) == test_tree.right


@pytest.mark.parametrize("p, q, expected", [(5, 1, 3), (5, 4, 5)])
def test_main(test_tree, p, q, expected):
    print("Test case start.")
    solution = Solution()
    common_ancestor = solution.lowestCommonAncestor(
        root=test_tree,
        p=find_node_by_name(test_tree, p),
        q=find_node_by_name(test_tree, q)
    )
    assert common_ancestor.val == expected
