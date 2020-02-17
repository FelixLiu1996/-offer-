class Solution:
    def match(self, s, pattern):
        if s and not pattern:
            return False
        elif not s and not pattern:
            return  True
        elif len(pattern) == 2 and pattern[1] == "*":
            return True
        elif len(s) == 0 and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2: ])
            else:
                return False
        else:
            if len(pattern) > 1 and pattern[1] == '*':
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2: ])
                else:
                    return self.match(s, pattern[2: ]) or self.match(s[1: ], pattern[2: ])\
                           or self.match(s[1: ], pattern)
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1: ], pattern[1: ])
                else:
                    return False
        # 这样 如果pattern的第二个是 * 的时候 考虑不完全
        # if len(pattern) == 2 and pattern[1] == '*':
        #     return True
        # s = list(s)
        # pattern = list(pattern)
        # if len(s) == len(pattern) - 2 and pattern[-1] == '*':
        #     pattern = pattern[:len(pattern) - 2]
        # i, j = 0, 0
        # while i < len(s) and j < len(pattern):
        #     if s[i] == pattern[j]:
        #         if j + 1 < len(pattern) and pattern[j + 1] == '*':
        #             temp = s[i]
        #             while i < len(s) and s[i] == temp:
        #                 i += 1
        #             j += 2
        #         else:
        #             i += 1
        #             j += 1
        #     elif pattern[j] == '.':
        #         i += 1
        #         j += 1
        #     elif s[i] != pattern[j] and pattern[j + 1] == '*':
        #         if pattern[j] != ".":
        #             j += 2
        #         else:
        #             return True
        #     else:
        #         return False
        # if i == len(s) and j == len(pattern):
        #     return True
        # return False
x = Solution()
print(x.match("'", "'"))