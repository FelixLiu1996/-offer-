class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        # 非递归
        # ans = ListNode(-1)
        # curr = ans
        # while pHead1 and pHead2:
        #     if pHead1.val > pHead2.val:
        #         curr.next = pHead2
        #         pHead2 = pHead2.next
        #         curr = curr.next
        #     else:
        #         curr.next = pHead1
        #         pHead1 = pHead1.next
        #         curr = curr.next
        # if pHead1:
        #     curr.next = pHead1
        # if pHead2:
        #     curr.next = pHead2
        # return ans.next

        # 递归
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val > pHead2.val:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1


