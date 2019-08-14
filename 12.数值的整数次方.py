class Solution:
    def Power(self, base, exponent):
        # 偷懒
        # return pow(base, exponent)

        ans = 1
        if exponent == 0:
            return 1
        elif exponent > 0:
            # 次方 > 0 的情况
            while exponent > 0:
                ans *= base
                exponent -= 1
        else:
            # 次方 < 0的情况
            exponent = -exponent
            while exponent > 0:
                ans /= base
                exponent -= 1
        return ans