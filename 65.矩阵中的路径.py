class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not path:
            return False
        visited = [0] * cols * rows
        pathLength = 0
        for i in range(rows):
            for j in range(cols):
                if self.find(matrix, i, j, rows, cols, path, pathLength, visited):
                    return True
        return False
    def find(self, matrix, i, j, rows, cols, path, pathLength, visited):
        if pathLength == len(path):
            return True
        hasPath = False
        if 0 <= i < rows and 0 <= j < cols and matrix[i * cols + j] == path[pathLength] and not visited[i * cols + j]:
            pathLength += 1
            visited[i * cols + j] = 1
            hasPath = self.find(matrix, i, j - 1, rows, cols, path, pathLength, visited) or \
                      self.find(matrix, i, j + 1, rows, cols, path, pathLength, visited) or \
                      self.find(matrix, i - 1, j, rows, cols, path, pathLength, visited) or \
                      self.find(matrix, i + 1, j, rows, cols, path, pathLength, visited)
            if not hasPath:
                pathLength -= 1
                visited[i * cols + j] = 0
        return hasPath
