class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        self.res = []
        self.middle_search(pRootOfTree)
        for idx, value in enumerate(self.res[:-1]):
            value.right = self.res[idx + 1]
            self.res[idx + 1].left = value
        return self.res[0]



    def middle_search(self, root):
        if not root:
            return
        self.middle_search(root.left)
        self.res.append(root)
        self.middle_search(root.right)
