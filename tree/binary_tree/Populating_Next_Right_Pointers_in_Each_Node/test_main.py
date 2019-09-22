import pytest
from tree.binary_tree.Populating_Next_Right_Pointers_in_Each_Node.main import Solution, Node

root = Node(val=1, left=Node(val=2, left=Node(val=4), right=Node(
    val=5)), right=Node(val=3, left=Node(val=6), right=Node(val=7)))

expected = Node(val=1, left=Node(val=2, left=Node(val=4), right=Node(
    val=5)), right=Node(val=3, left=Node(val=6), right=Node(val=7)))
# 2 -> 3
expected.left.next = expected.right
# 4 -> 5
expected.left.left.next = expected.left.right
# 5 -> 6
expected.left.right.next = expected.right.left
# 6 -> 7
expected.right.left.next = expected.right.right

solution = Solution()
answer = solution.connect(root)
# 2 -> 3
assert expected.left.next.val == answer.left.next.val
# 4 -> 5
assert expected.left.left.next.val == answer.left.left.next.val
# 5 -> 6
assert expected.left.right.next.val == answer.left.right.next.val
# 6 -> 7
assert expected.right.left.next.val == answer.right.left.next.val
