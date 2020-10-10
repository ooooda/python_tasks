# https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        cnt = 0
        cur = head
        if cur.next == None:
            return head
        while cur.next != None:
            length += 1
            cur = cur.next
        cur = head
        if length % 2 == 0:
            length = length // 2
        else:
            length = length // 2 + 1
        while cnt != length:
            cur = cur.next
            result = cur
            cnt += 1
        return result