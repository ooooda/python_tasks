# linked-list

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

+ [Linked List Cycle](#linked-list-cycle)

+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)

+ [Linked List Cycle II](#linked-list-cycle-ii)

+ [Reorder List](#reorder-list)

+ [Palindrome Linked List](#palindrome-linked-list)

+ [Sort List](#sort-list)

+ [Middle of the Linked List](#middle-of-the-linked-list)

+ [Reverse Linked List](#reverse-linked-list)

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/


```python

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

```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/


```python

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

```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/


```python

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

```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/


```python

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

```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/


```python

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


```

## Reorder List

https://leetcode.com/problems/reorder-list/


```python

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




```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/


```python

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        cur = head
        check = []
        while cur != None:
            check.append(cur.val)
            cur = cur.next
        if check == check[::-1]:
            return True
        return False

```

## Sort List

https://leetcode.com/problems/sort-list/


```python

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

```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/


```python

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

```

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/


```python

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


```

