class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintFromTopToBottom(self, root):
        # 二叉树的层次遍历
        # 用队列来实现
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            temp = queue.pop(0)
            ans.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return ans
