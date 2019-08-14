class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # curr = ListNode()
        curr = listNode
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        ans[:] = ans[::-1]
        return ans

