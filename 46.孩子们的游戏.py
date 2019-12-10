class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        children = [i for i in range(n)]
        curr = 0
        while len(children) > 1:
            for i in range(1, m):
                curr += 1
                # 如果到了数组最后 变成头部
                if curr == len(children):
                    curr = 0
            children.remove(children[curr])
            if curr == len(children):
                curr = 0
        return children[0]