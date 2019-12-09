class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)

x = Solution()
print(x.GetNumberOfK([1,1,2,2], 1))