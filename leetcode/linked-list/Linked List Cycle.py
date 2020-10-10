# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        if head == None or head.next == None or head.next.next == None:
            return False
        else:
            fast = head.next.next
        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True