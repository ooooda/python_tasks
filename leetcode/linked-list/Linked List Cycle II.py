# https://leetcode.com/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        cur = head
        passed = set()
        cnt = 0
        while True:
            if cur.next == None:
                return None
            else:
                if cur not in passed:
                    passed.add(cur)
                else:
                    return cur
                cur = cur.next
