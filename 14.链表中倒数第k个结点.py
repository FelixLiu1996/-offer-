class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # 用数组去存
        # if not head:
        #     return None
        # ls = []
        # while head:
        #     ls.append(head)
        #     head = head.next
        # if k > len(ls):
        #     return None
        # return ls[-k]

        # 快慢指针
        # 快指针先走k - 1步，然后慢指针走
        # 快指针走到链表尾，慢指针走到倒数第k个结点
        if (not head) or (k == 0):
            return None
        fast = slow = head
        while k > 1:
            if fast.next:
                fast = fast.next
                k -= 1
            else:
                return None

        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow
