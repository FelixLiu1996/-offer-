class Solution:
    def __init__(self):
        self.str = ''
        self.dict = {}

    def FirstAppearingOnce(self):
        for s in self.str:
            if self.dict[s] == 1:
                return s
        return "#"

    def Insert(self, char):
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
        if self.dict[char] == 1:
            self.str += self.str + char