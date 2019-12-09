class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # 双指针
        right = len(array) - 1
        left = 0
        while left < right:
            if array[left] + array[right] < tsum:
                left += 1
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                return [array[left], array[right]]
        return []