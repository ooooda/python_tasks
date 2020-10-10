# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == l2 and l1 == None:
            return l1
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        cur1 = l1
        cur2 = l2
        if cur1.val > cur2.val:
            cur1 = l2
            cur2 = l1
            x = l2
        else:
            x = l1
        while cur1 != None:
            if cur1.next != None:
                if cur1.val <= cur2.val <= cur1.next.val:
                    dop = cur1.next
                    cur1.next = cur2
                    cur2 = dop
            else:
                if cur2 != None:
                    cur1.next = cur2
                    break
            cur1 = cur1.next
        return x