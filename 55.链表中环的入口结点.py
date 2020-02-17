class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead is None or pHead.next is None or pHead.next.next is None:
            return None
        slow, fast = pHead, pHead
        while fast and fast.next:
            # 在快慢指针第一次相遇之后，
            # 让两个慢指针一个从链表头出发 另一个从相遇位置出发，步长为1
            # 再次相遇的地方就是环的入口结点
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p1, p2 = pHead, slow
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1

        return None

        # slow, fast = pHead, pHead
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         break
        #
        # if not fast or not fast.next:
        #     return None
        # p1 = pHead
        # while p1 != slow:
        #     p1 = p1.next
        #     slow = slow.next
        # return p1