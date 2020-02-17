class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        node_list = [pRoot]
        ans = []
        while node_list:
            ans_each = []
            temp = []
            for i in node_list:
                ans_each.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            ans.append(ans_each)
            node_list = temp
        return ans