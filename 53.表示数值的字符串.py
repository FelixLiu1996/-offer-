class Solution:
    def isNumeric(self, s):
        sign, science_e, point = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "+" or s[i] == '-':
                sign += 1
                # 如果是第一次出现，且不是第一位，那么必须在e E 后面
                if sign == 1 and i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    print(f'no {s[i - 1]}')
                    return False
                # 如果是第二次出现，则必须要在e E 后面
                if sign == 2 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif s[i] == '.':
                point += 1
                # 如果是第一次出现，如果是在e 后面出现的 则不行 且小数点不能第一位出现
                if point == 1 and i == 0:
                    return False
                # 如果是第二次出现
                if point == 2 or science_e == 1:
                    return False
            elif s[i] == 'e' or s[i] == 'E':
                science_e += 1
                if science_e == 2:
                    return False
                else:
                    # 如果是第一次出现，则不能是最后出现
                    if i == len(s) - 1:
                        return False
            else:
                # 其他的只能是数字
                if s[i] not in '1234567890':
                    return False
        return True

x = Solution()
print(x.isNumeric("123.6e+1"))