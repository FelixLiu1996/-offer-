class Solution:
    def rectCover(self, number):
        # 就是斐波那契数列
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            a, b = 1, 2
            i = 3
            while i <= number:
                a, b = b, a + b
                i += 1
            return b

        # 递归超时
        # if number == 0:
        #     return 0
        # elif number == 1:
        #     return 1
        # elif number == 2:
        #     return 2
        # else:
        #     return self.rectCover(number - 1) + self.rectCover(number - 2)

x = Solution()
print(x.rectCover(5))