class Solution:
    def FirstNotRepeatingChar(self, s):
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i, 1]
            else:
                dic[s[i]][1] += 1
        ans = 10010
        for value in dic.values():
            if value[1] == 1:
                if ans > value[0]:
                    ans = value[0]
        if ans == 10010:
            return -1
        else:
            return ans

x = Solution()
print(x.FirstNotRepeatingChar('google'))