class TreeNode:
    def __init__(self, x: int):
        self.val = x
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


INF = int(1e16)


class Solution:
    def successor(self, node: TreeNode):
        node = node.right
        while node.left:
            node = node.left
        return node

    def predecessor(self, node: TreeNode):
        node = node.left
        while node.right:
            node = node.right
        return node

    def closestValue(self, root: TreeNode, target: float) -> int:
        print(root.val, root.left, root.right)
        res = abs(target - root.val)
        pred_res = abs(target - self.predecessor(root).val) if root.left else INF
        succ_res = abs(target - self.successor(root).val) if root.right else INF
        if res > pred_res:
            return self.closestValue(root.left, target)
        elif res > succ_res:
            return self.closestValue(root.right, target)
        else:
            return root.val

