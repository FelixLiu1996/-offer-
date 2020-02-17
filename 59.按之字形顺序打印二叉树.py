class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        flag = 1   # 记录是奇数行还是偶数行
        stack_or_queue = [pRoot]
        ans = []
        while stack_or_queue:
            print_line = []
            temp = []
            for i in stack_or_queue:
                print_line.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            # 奇数行直接按顺序打印 偶数行反转之后再打印
            if flag % 2 != 0:
                ans.append(print_line)
            else:
                print_line = print_line[::-1]
                ans.append(print_line)
            stack_or_queue = temp
            flag += 1
        return ans



