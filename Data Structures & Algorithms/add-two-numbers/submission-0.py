# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ""
        p = l1
        while p:
            s += str(p.val)
            p = p.next
        n1 = int(s[::-1])
        p = l2
        s = ""
        while p:
            s += str(p.val)
            p = p.next
        n2 = int(s[::-1])
        sm = n1 + n2
        sm = (str(sm))
        sm = sm[::-1]
        head = None
        p = None
        for v in sm:
            value = int(v)
            n = ListNode(value)
            if head is None:
                head = n
                p = head
            else:
                p.next = n
                p = p.next
        return head
        