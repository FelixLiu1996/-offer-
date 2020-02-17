class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        newHead = ListNode(0)
        newHead.next = pHead
        curr, check = newHead, newHead.next
        while check:
            if check.next is not None and check.val == check.next.val:
                # 一直找到最后一个相同的结点
                while check.next is not None and check.val == check.next.val:
                    check = check.next
                curr.next = check.next
                check = check.next
            else:
                curr = curr.next
                check = check.next
        return newHead.next

