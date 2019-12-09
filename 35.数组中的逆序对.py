class Solution:
    # 暴力法超时
    # def InversePairs(self, data):
    #     ans = 0
    #     for i in range(len(data) - 1):
    #         temp = data[i]
    #         for j in range(i + 1, len(data)):
    #             if temp > data[j]:
    #                 ans += 1
    #     return ans % 1000000007
    def InversePairs(self, data):
        num, new_lsit = self.mergeSort(data)
        return num % 1000000007

    def mergeSort(self, data):
        # 归并排序
        def merge(left, right):
            inverse_num = 0
            result = []
            i = j = 0
            while i < len(left)  and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    # 说明比左边的剩下的数都要大
                    inverse_num += len(left) - i

            result = result + left[i:] + right[j:]
            return inverse_num, result
        if len(data) <= 1:
            return 0, data
        else:
            mid = len(data) // 2
            num_left, left = self.mergeSort(data[:mid])
            num_right, right = self.mergeSort(data[mid:])
            num_merge, new_list = merge(left, right)
            inverse_num = num_left + num_right + num_merge
            return inverse_num, new_list

x = Solution()
print(x.InversePairs([1,2,3,4,5,6,7,0]))