# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cnt = 0
        if head == None:
            return head
        if head.next == None and n == 1:
            return head.next
        if head.next == None and n != 1:
            return head
        cur = head
        prev = None
        while cur != None:
            if cnt != n:
                cnt += 1
            else:
                if prev == None:
                    prev = head
                else:
                    prev = prev.next
            cur = cur.next
        if prev == None:
            head = head.next
        else:
            if prev.next != None:
                future = prev.next.next
            else:
                future = None
            prev.next = future
        return head