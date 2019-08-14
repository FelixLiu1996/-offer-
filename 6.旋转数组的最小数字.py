class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # 偷懒法
        # return min(rotateArray)

        # 根据是非减排序的数组的旋转，所以当出现前一个元素值大于后一个元素值时说明此处是旋转点
        # i = 0
        # while i < len(rotateArray):
        #     if rotateArray[i] > rotateArray[i + 1]:
        #         return rotateArray[i + 1]
        #     i += 1

        # 二分查找
        left, right = 0, len(rotateArray) - 1
        while left < right:
            mid = (left + right) // 2
            if rotateArray[mid] > rotateArray[right]:
                # 如果中间值比右端值大，则说明旋转点在右边
                left = mid + 1
            elif rotateArray[mid] <= rotateArray[right]:
                # 如果中间值比左端值小，则说明旋转点在左边
                right = mid
        return rotateArray[left]