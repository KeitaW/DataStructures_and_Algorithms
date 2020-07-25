from typing import List


class TreeNode:
    def __init__(self, x: int, cnt: int):
        self.val = x
        self.cnt = cnt  # How many # of nodes are under it
        self.left = None
        self.right = None

    def __str__(self, level=0, right=False):
        return (
            "    " * (level - 1)
            + (" └──" if right else (" ├──" if level != 0 else ""))
            + " "
            + str(self.val)
            + "\n"
            + (self.left.__str__(level + 1, False) if self.left else "")
            + (self.right.__str__(level + 1, True) if self.right else "")
        )


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        for num in nums:
            self.root = self.insert(self.root, num)

    def insert(self, cur: TreeNode, val: int) -> TreeNode:
        if cur is None:
            return TreeNode(val, 1)
        elif cur.val > val:
            cur.left = self.insert(cur.left, val)
        else:
            cur.right = self.insert(cur.right, val)
        cur.cnt += 1
        return cur

    def searchKth(self, cur: TreeNode, k: int) -> int:
        # m: size of the right subtree
        # ⇔ cur is m+1 th largest node in the BST
        m = cur.right.cnt if cur.right is not None else 0
        if k == m + 1:
            return cur.val
        elif k <= m:
            # we want to investigate larger nodes
            return self.searchKth(cur.right, k)
        else:
            return self.searchKth(cur.left, k - m - 1)

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        return self.searchKth(self.root, self.k)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
