class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        # 第一种方法
        # curr = pHead
        # rev = None
        # while curr:
        #     curr, rev , rev.next = curr.next, curr, rev
        # return rev

        # 第二种方法
        val = []
        curr = pHead
        while curr:
            val.append(curr.val)
            curr = curr.next
        curr2 = pHead
        while curr2:
            curr2.val = val.pop()
            curr2 = curr2.next
        return pHead
