class Solution:
    def FindGreatestSumOfSubArray(self, array):
        ans = array[0]
        temp = 0
        for i in array:
            if temp > 0:
                temp += i
            else:
                temp = i
            if ans < temp:
                ans = temp
        return ans


x = Solution()
print(x.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))