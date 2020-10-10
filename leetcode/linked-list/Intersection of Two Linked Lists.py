# https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def find_common(self, head, i):
        used = set()
        if i == -1:
            while head.next != None:
                head = head.next
            return head
        if i == 1:
            while head != None:
                used.add(head)
                head = head.next
            return used

    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> ListNode:
        if head1 == None or head2 == None:
            return None
        met = set()
        met.add(self.find_common(head1, -1))
        compare = self.find_common(head2, -1)
        if compare not in met:
            return None
        else:
            met = self.find_common(head1, 1)
            cur = head2
            while cur != None:
                if cur in met:
                    return cur
                cur = cur.next