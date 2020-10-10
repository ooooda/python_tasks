# https://leetcode.com/problems/palindrome-linked-list/
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