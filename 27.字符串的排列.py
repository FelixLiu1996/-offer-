class Solution:
    def Permutation(self, ss):
        if not ss:
            return None
        ans = []
        self.helper(ss, ans, '')
        ans = list(set(ans))
        ans.sort()
        return ans

    def helper(self, ss, ans, ans_each):
        if not ss:
            ans.append(ans_each)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i + 1: ], ans, ans_each + ss[i])
