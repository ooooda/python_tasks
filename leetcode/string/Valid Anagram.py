# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = []
        t_letters = []
        if len(s) != len(t):
            return False
        for el in s:
            s_letters.append(ord(el))
        for el in t:
            t_letters.append(ord(el))
        s_letters.sort()
        t_letters.sort()
        if t_letters == s_letters:
            return True
        return False