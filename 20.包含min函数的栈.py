class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        self.stack.append(node)
        if not self.minstack or node < self.minstack[-1]:
            self.minstack.append(node)
    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()


    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minstack[-1]