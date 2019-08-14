class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # 递归版本
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        bt = TreeNode(pre[0])
        bt.left = self.reConstructBinaryTree(pre[1: tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
        bt.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return bt