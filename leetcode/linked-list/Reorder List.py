# https://leetcode.com/problems/reorder-list/
class Solution:
    def reverseList(self, head):
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

    def split(self, head):
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

    def reorderList(self, head: ListNode) -> None:
        if head != None and head.next != None and head.next.next != None:
            cur1, cur2 = self.split(head)
            cur2 = self.reverseList(cur2)
            helper = cur1
            use = cur1
            while helper is not None:
                helper = helper.next
                if cur2 is not None:
                    use.next = cur2
                    use = use.next
                    cur2 = cur2.next
                use.next = helper
                use = use.next
            head = cur1
        else:
            return head

