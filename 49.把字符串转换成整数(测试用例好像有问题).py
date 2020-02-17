# 这一题测试用例好像有问题
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        dic = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
               "7": 7, "8": 8, "9": 9, "0": 0 }
        ans = 0
        check = 1
        s = list(s)
        if s[0] == '+':
            check = 1
            s.pop(0)
        elif s[0] == '-':
            check = -1
            s.pop(0)
        for temp in s:
            if temp in dic:
                ans = ans * 10 + dic[temp]
            else:
                return 0
        return check * ans
x = Solution()
print(x.StrToInt('2147483647'))
