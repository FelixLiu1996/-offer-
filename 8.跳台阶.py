class Solution:
    def jumpFloor(self, number):
        # 斐波那契数列
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            Fn = [0, 1]
            i = 1
            while i <= number:
                Fn.append(Fn[i] + Fn[i - 1])
                i += 1
            return Fn[number + 1]
