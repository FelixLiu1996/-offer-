class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        curr1 = pHead1
        curr2 = pHead2
        stack1, stack2 = [], []
        while curr1:
            stack1.append(curr1)
            curr1 = curr1.next
        while curr2:
            stack2.append(curr2)
            curr2 = curr2.next
        ans = []
        while stack1 and stack2:
            temp1 = stack1.pop()
            temp2 = stack2.pop()
            if temp1 == temp2:
                ans.append(temp1)

        if ans:
            ans = ans.pop()
            return ans


