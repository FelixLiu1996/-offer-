class Solution:
    def ReverseSentence(self, s):
        temp_string = s.split(" ")
        ans = ''
        for i in range(len(temp_string) - 1, -1, -1):
            if i != 0:
                ans += temp_string[i] + ' '
            else:
                ans += temp_string[i]
        return ans

x = Solution()
print(x.ReverseSentence("I am a student."))