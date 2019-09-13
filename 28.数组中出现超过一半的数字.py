class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # numbers_set = set(numbers)
        # ans = 0
        # half = len(numbers) // 2
        # for i in numbers_set:
        #     temp = numbers.count(i)
        #     if temp > half:
        #         ans = i
        # return ans

        
        dic = {}
        half = len(numbers) // 2
        if  len(numbers) == 1:
            return numbers[0]
        for i in numbers:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                if dic[i] > half:
                    return i
        return 0


