class Solution:
    def FindNumsAppearOnce(self, array):
        dic = {}
        for i in array:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        ans = []
        for key, value in dic.items():
            if value == 1:
                ans.append(key)
        return ans