class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        return abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) <= 1 and \
               self.IsBalanced_Solution(pRoot.left) and \
               self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))