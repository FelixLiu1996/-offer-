class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def KthNode(self, pRoot, k):
        if not pRoot:
            return None
        self.res = []
        self.middle_search(pRoot)
        if k > len(self.res) or k <= 0:
            return None
        return self.res[k - 1]

    def middle_search(self, root):
        # 二叉搜索树的中序遍历 自带顺序性
        if not root:
            return
        self.middle_search(root.left)
        self.res.append(root)
        self.middle_search(root.right)