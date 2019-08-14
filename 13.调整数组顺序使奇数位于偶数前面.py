class Solution:
    def reOrderArray(self, array):
        # 开两个数组，一个存奇数，一个存偶数
        array_odd = []
        array_even = []
        for num in array:
            if num % 2 == 0:
                array_even.append(num)
            else:
                array_odd.append(num)
        ans = array_odd + array_even
        return ans
        