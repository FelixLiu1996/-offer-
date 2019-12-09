class Solution:
    def LeftRotateString(self, s, n):
        return s[n:] + s[0: n]

x = Solution()
print(x.LeftRotateString('abcdefg',2))