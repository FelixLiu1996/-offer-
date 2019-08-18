class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return None
        res = []  # 辅助栈
        # 入栈顺序与出栈顺序的对比，可以重新入栈进行判断
        # 使用辅助栈进行入栈顺序与出栈顺序的对比
        # 将入栈的第一个元素压入辅助栈，将辅助栈栈顶元素与出栈的第一个元素进行对比
        # 若不相等则继续压入，若相等，则将辅助栈栈顶元素与出栈的第一个元素弹出
        # 依次类推，相等则弹出，不相等则压入，最后若辅助栈的元素为空，则说明是出栈顺序，否则不是
        while pushV:
            if not res or popV[0] != res[-1]:
                res.append(pushV.pop(0))
            elif popV[0] == res[-1]:
                # 如果辅助栈的栈顶与出栈底层元素相同，则弹出
                res.pop()
                popV.pop(0)
        while res and popV:
            if res[-1] == popV[0]:
                res.pop()
                popV.pop(0)
            else:
                break
        return not res