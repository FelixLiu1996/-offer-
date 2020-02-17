class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        visited = [[0 for i in range(cols)] for j in range(rows)]
        self.findWay(visited, 0, 0, rows, cols, threshold)
        return self.count

    def findWay(self, visited, i, j, rows, cols, k):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return
        digit_i = list(map(int, str(i)))
        digit_j = list(map(int, str(j)))
        if sum(digit_i) + sum(digit_j) > k or visited[i][j] == 1:
            return
        visited[i][j] = 1
        self.count += 1
        self.findWay(visited, i - 1, j, rows, cols, k)
        self.findWay(visited, i + 1, j, rows, cols, k)
        self.findWay(visited, i, j - 1, rows, cols, k)
        self.findWay(visited, i, j + 1, rows, cols, k)