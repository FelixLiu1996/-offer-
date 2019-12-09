import math
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        n = int(math.sqrt(2 * tsum))
        ans = []
        for i in range(n, 2, -1):
            ans_each =[]
            if i % 2 == 0:
                # 如果是偶数个的情况
                mid = int(tsum / i)
                head = int(mid - (i / 2) + 1)
                if i * head + i * (i - 1) / 2 == tsum:
                    ans_each = [j for j in range(head, head + i)]
                    ans.append(ans_each)
            else:
                # 如果是奇数的情况下
                mid = int(tsum / i)
                head = mid - int(i / 2)
                if i * head + i * (i - 1) / 2 == tsum:
                    ans_each = [j for j in range(head, head + i)]
                    ans.append(ans_each)
        if tsum % 2 != 0 and tsum > 1:
            # 说明是奇数 才有可能两个相邻相加得到
            ans.append([tsum // 2, tsum // 2 + 1])
        return ans



