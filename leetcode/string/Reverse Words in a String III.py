# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        j = 0
        for i, el in enumerate(s):
            if el == ' ':
                s[j:i] = s[j:i][::-1]
                j = i + 1
            elif i == len(s) - 1:
                s[j:i + 1] = s[j:i + 1][::-1]
        s = ''.join(s)
        return s


