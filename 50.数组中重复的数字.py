class Solution:
    def duplicate(self, numbers, duplication):
        check_set = set()
        for num in numbers:
            if num not in check_set:
                check_set.add(num)
            else:
                duplication[0] = num
                return True
        return False