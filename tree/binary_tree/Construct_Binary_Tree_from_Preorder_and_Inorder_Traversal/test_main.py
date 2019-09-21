import pytest
from main import Solution

solution = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
solution.buildTree(preorder, inorder)
