class Solution:
    def Find(self, target, array):
        # if array == [[]]:
        #     return False
        # for i in range(len(array)):
        #     if target in array[i]:
        #         return True
        # return False

        if array == [[]]:
            return False
        # 因为有序，所以将每一行进行二分查找
        for i in range(len(array)):
            left, right = 0, len(array[i]) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[i][mid] > target:
                    # 说明target在mid的左边
                    right = mid - 1
                elif array[i][mid] < target:
                    left = mid + 1
                else:
                    return True
        return False
