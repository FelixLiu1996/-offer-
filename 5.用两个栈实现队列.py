class Solution:
    def __init__(self):
        # 两个栈，一个作为压入栈，一个作为弹出栈
        self.push_stack = []
        self.pop_stack = []

    def push(self, node):
        self.push_stack.append(node)

    def pop(self):
        if self.pop_stack == []:
            # 如果要做弹出的栈为空的话，将作为压入栈的栈中的元素分别倒序压入弹出栈
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()
        else:
            # 如果弹出栈不为空，则弹出栈顶元素，返回弹出栈即可
            return self.pop_stack.pop()
