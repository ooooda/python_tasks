# https://leetcode.com/problems/sort-list/
class Solution:
    def middleNode(self, head):
        length = 0
        cnt = 0
        cur = head
        cur1 = head
        cur11 = cur1
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
        while cur11.next != result:
            cur11 = cur11.next
        cur11.next = None
        cur2 = result
        return cur1, cur2

    def mergeTwoLists(self, l1, l2):
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

    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        cur1, cur2 = self.middleNode(cur)
        x = self.sortList(cur1)
        y = self.sortList(cur2)
        z = self.mergeTwoLists(x, y)
        return z