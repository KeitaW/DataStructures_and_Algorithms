# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse_tree(node):
            """Check if subtree starts from node contains both  p and q.
            """
            if node is None:
                return False
            print(f"Current node is {node.val}")
            left = traverse_tree(node.left)
            right = traverse_tree(node.right)
            print(f"Left and Right for Node {node.val}: {left}, {right}")
            # Current node is either p or q
            mid = (node == p) or (node == q)
            # Any two of the flags become true <-> both p and q are in the same subtree.
            if mid + left + right >= 2:
                self.ans = node
            if self.ans:
                print(f"Current ans is {self.ans.val}")
            return mid or left or right
        traverse_tree(root)
        return self.ans


# class Solution:
#    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#        # 方針: Inorder searchをしてリストを作る
#        # ２つのノードが別のリストに格納されるまでリストを分割する
#        def get_inorder_list(root):
#            def func(node):
#                print(node)
#                if node is None:
#                    return
#                func(node.left)
#                inorder_list.append(node.val)
#                func(node.right)
#            func(root)
#        inorder_list = []
#        get_inorder_list(root)
#        inorder_tabel = {val: idx for idx, val in enumerate(inorder_list)}
#
#        def devide_and_check(in_list, idx, prev_idx):
#            if not (p in in_list and q in in_list):
#                return
#            if not (p in in_list or q in in_list):
#                return prev_index
#            devide_and_check()
#
#        return root
#
