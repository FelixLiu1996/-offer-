class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        # 0 不在numbers里面的情况
        if 0 not in numbers:
            if len(set(numbers)) != len(numbers):
                return False
            else:
                if max(numbers) - min(numbers) == 4:
                    return True
                else:
                    return False
        else:
            # 0 在的情况
            num_zero = numbers.count(0)
            numbers.sort()
            # 去掉有对子的情况
            if len(set(numbers[num_zero:])) != len(numbers[num_zero: ]):
                return False
            # 记录差值的多少 只有差值大于1 则记录有差值 差值小于0的个数才是顺子
            # 如 2 4 0   可以4 - 2 - 1 = 1 == 0的个数
            diff = 0
            for i in range(num_zero + 1, len(numbers)):
                diff += numbers[i] - numbers[i - 1] - 1
            if diff > num_zero:
                return False
            else:
                return True

x = Solution()
print(x.IsContinuous([0,3,1,6,4]))