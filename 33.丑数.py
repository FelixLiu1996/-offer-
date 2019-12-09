class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        ugly_num = [1]
        index_2, index_3, index_5 = 0, 0, 0
        for i in range(index - 1):
            ugly_num.append(min(ugly_num[index_2] * 2, ugly_num[index_3] * 3, ugly_num[index_5] * 5))
            if ugly_num[-1] == ugly_num[index_2] * 2:
                index_2 += 1
            if ugly_num[-1] == ugly_num[index_3] * 3:
                index_3 += 1
            if ugly_num[-1] == ugly_num[index_5] * 5:
                index_5 += 1
        return ugly_num[-1]