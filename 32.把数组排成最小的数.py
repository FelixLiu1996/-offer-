import functools
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        def cmp_str(a, b):
            """
            :return: 如果 字符串ab > ba, 那么a > b 返回1 表示 a > b
            如果 ab < ba, 那么 a < b 返回-1，表示a < b
            如果ab = ba，那么a=b 返回0，表示a=b
            使用functools里的函数完成自定义排序
            """
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0
        numbers = [str(i) for i in numbers]
        numbers = sorted(numbers, key=functools.cmp_to_key(cmp_str))
        numbers = ''.join(numbers)
        return numbers
x = Solution()
print(x.PrintMinNumber([3, 321, 32]))