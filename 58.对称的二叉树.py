class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        else:
            return self.checkSymmetrical(pRoot.left, pRoot.right)

    def checkSymmetrical(self, left, right):
        if left is None and right is None:
            return True
        if (left is not None and right is None) or (left is None and right is not None):
            return False
        if left is not None and right is not None:
            if left.val != right.val:
                return False
            else:
                return self.checkSymmetrical(left.left, right.right) and self.checkSymmetrical(left.right, right.left)