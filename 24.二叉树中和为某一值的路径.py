class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        result = []
        self.find_path(expectNumber, 0, [], root, result)
        return result

    def find_path(self, expectNumber, curr_sum, curr_path, root, result):

        curr_sum += root.val
        curr_path.append(root)
        if curr_sum == expectNumber and (not root.left and not root.right):
            # 如果当前是叶节点且值为期望值
            path = []
            for i in curr_path:
                path.append(i.val)
            result.append(path)

        if curr_sum < expectNumber:
            if root.left:
                self.find_path(expectNumber, curr_sum, curr_path, root.left, result)
            if root.right:
                self.find_path(expectNumber, curr_sum, curr_path, root.right, result)
        curr_path.pop()


