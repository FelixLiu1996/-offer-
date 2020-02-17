class Solution:
    def maxInWindows(self, num, size):
        maxList = []
        if size == 0 or len(num) < size:
            return []
        for idx in range(size - 1, len(num)):
            maxList.append(max(num[idx - size + 1: idx + 1]))
        return maxList