# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        is_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels_in_text = []
        s_dublet = ''
        cnt = 0
        for i, el in enumerate(s):
            if el in is_vowels:
                vowels_in_text.append(el)

        vowels_in_text = vowels_in_text[::-1]

        for i, el in enumerate(s):
            if el in is_vowels:
                s_dublet += vowels_in_text[cnt]
                cnt += 1
            else:
                s_dublet += el
        return s_dublet