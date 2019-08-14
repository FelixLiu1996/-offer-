class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        ans = False
        # 进行遍历，如果子树的值相等，则看以此为根节点的子树是否有相同结构
        if pRoot1.val == pRoot2.val:
            ans = self.check_sub_tree(pRoot1, pRoot2)
        if not ans:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        return ans

    def check_sub_tree(self, pRoot1, pRoot2):
        # 这个if不能和下面的调换顺序
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.check_sub_tree(pRoot1.left, pRoot2.left) and self.check_sub_tree(pRoot1.right, pRoot2.right)