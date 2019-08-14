class Solution:
    def Fibonacci(self, n):
        # 递推法
        x, y = 0, 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            i = 2
            f_n = 0
            while i <= n:
                f_n = x + y
                x, y = y, f_n
                i += 1
            return f_n

        # 递归法超时
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

