class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        ans = 0
        i = 1
        while i <= n:
            temp = i * 10
            ans += (n // temp) * i
            if n % temp > (2 * i - 1):
                ans += i
            elif (i - 1) < n % temp <= (2 * i - 1):
                ans += (n % temp) - i + 1
            i *= 10
        return ans

x = Solution()
print(x.NumberOf1Between1AndN_Solution(13))