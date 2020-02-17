class Solution:
    # def cutRope(self, number):
    #     if number == 2:
    #         return 1
    #     if number == 3:
    #         return 2
    #     # 剪出来的数只有可能是2 或者 3
    #     # 只是看2 和 3 的倍数  以为2 * 2 * 2 < 3 * 3  所以 2 的个数肯定比3要少
    #     # 有没有2 可以看number // 3 有没有余数 整除则没有2，
    #     # 余数是1的话 可以去掉一个3 从 3 * 1 变成 2 * 2
    #     # 余数是2的话，那就是多一个2
    #     x = number % 3
    #     y = number // 3
    #     if x == 0:
    #         return 3 ** y
    #     elif x == 1:
    #         return 2 * 2 * 3 ** (y - 1)
    #     else:
    #         return 2 * 3 ** y

    # 动态规划
    def cutRope(self, number):
        if number == 2:
            return 1
        if number == 3:
            return 2
        prod = [1, 2, 3]
        for i in range(4, number + 1):
            max_number = 0
            for j in range(1, i // 2 + 1):
                temp = prod[j] * prod[i - j]
                if temp > max_number:
                    max_number = temp
            prod.append(max_number)
        return prod[-1]