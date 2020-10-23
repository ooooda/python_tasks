# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        if l != 0:
            for i in range(l):
                if i < len(s) - i:
                    s[i], s[l - 1 - i] = s[l - 1 - i], s[i]