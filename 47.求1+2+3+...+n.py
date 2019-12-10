class Solution:
    def Sum_Solution(self, n):
        # 不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
        ans = n
        # 短路求法  如果and前面为真 则输出后面的值
        return ans and (ans + self.Sum_Solution(n - 1))
