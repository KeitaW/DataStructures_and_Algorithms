import pytest
from main import Solution

solution = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
solution.buildTree(inorder, postorder)
