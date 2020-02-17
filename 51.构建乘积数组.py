class Solution:
    def multiply(self, A):
        B = [1 for i in range(len(A))]
        # 计算下三角
        length = len(A)
        for i in range(1, length):
            B[i] = B[i - 1] * A[i - 1]
        # 计算下三角
        temp = 1
        for j in range(length - 2, -1, -1):
            temp *= A[j + 1]
            B[j] *= temp
        return B
