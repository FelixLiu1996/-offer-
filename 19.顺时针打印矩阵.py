class Solution:
    def printMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        di, dj = 0, 1  # 表示方向的变量
        i, j = 0, 0
        for k in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = False
            # 判断是否转向
            if matrix[(i + di) % m][(j + dj) % n] == False:
                di, dj = dj, -di
            i += di
            j += dj
        return ans
