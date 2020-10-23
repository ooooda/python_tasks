# https://leetcode.com/problems/to-lower-case/
class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        dif = ord('A') - ord('a')
        for i, el in enumerate(s):
            if 'A' <= el <= 'Z':
                s[i] = chr(ord(el) - dif)
        s = ''.join(s)
        return s