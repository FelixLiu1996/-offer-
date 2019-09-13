class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # if k > len(tinput):
        #     return []
        # tinput.sort()
        # return tinput[:k]


        # 练习快排
        if k > len(tinput):
            return []
        self.quick_sort(tinput, 0, len(tinput) - 1)
        return tinput[: k]
    def quick_sort(self, array, left, right):
        if left > right:
            return
        key = array[left]
        i, j = left, right
        while i != j:
            while array[j] >= key and i < j:
                j -= 1
            while array[i] <= key and i < j:
                i += 1
            if i < j:
                array[i], array[j] = array[j], array[i]
        # 交换基准数和相遇的位置的数
        array[left], array[i] = array[i], array[left]
        self.quick_sort(array, left, i - 1)
        self.quick_sort(array, i + 1, right)

