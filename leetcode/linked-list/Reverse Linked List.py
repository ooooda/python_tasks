# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        cur = head
        prev = None
        while cur != None:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        return prev
