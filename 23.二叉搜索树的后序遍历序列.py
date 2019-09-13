class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return self.check(sequence, 0)
    def check(self, sequence, left):
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        while sequence[left] < root:
            left += 1
        for j in range(left, len(sequence) - 1):
            if sequence[j] < root:
                return False
        sequence_left, sequence_right = sequence[:left], sequence[left:len(sequence) - 1]
        left_ans, right_ans = True, True
        if len(sequence_left) > 0:
            left_ans = self.check(sequence_left, 0)
        if len(sequence_right) > 0:
            right_ans = self.check(sequence_right, 0)
        return left_ans and right_ans


