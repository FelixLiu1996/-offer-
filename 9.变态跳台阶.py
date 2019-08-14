class Solution:
    def jumpFloorII(self, number):
        # 斐波那契数列的变种
        # 即 f(n) = f(n - 1) + f(n - 2) + ... + f(1)
        # f(n - 1) = f(n - 2) + ... + f(1)
        # 两式减得 f(n) = 2f(n - 1)
        # f(1) = 1
        ans = 1
        for i in range(2, number + 1):
            ans = 2 * ans
        return ans

        # return pow(2, number - 1)