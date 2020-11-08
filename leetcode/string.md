# string

+ [To Lower Case](#to-lower-case)

+ [Reverse String](#reverse-string)

+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)

+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

+ [Valid Anagram](#valid-anagram)

## To Lower Case

https://leetcode.com/problems/to-lower-case/


```python

class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        dif = ord('A') - ord('a')
        for i, el in enumerate(s):
            if 'A' <= el <= 'Z':
                s[i] = chr(ord(el) - dif)
        s = ''.join(s)
        return s

```

## Reverse String

https://leetcode.com/problems/reverse-string/


```python

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        if l != 0:
            for i in range(l):
                if i < len(s) - i:
                    s[i], s[l - 1 - i] = s[l - 1 - i], s[i]

```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/


```python

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

```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/


```python

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






```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/


```python

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

```

