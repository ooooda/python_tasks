# math

+ [Palindrome Number](#palindrome-number)

+ [Fibonacci Number](#fibonacci-number)

+ [Reverse Integer](#reverse-integer)

+ [Sqrt(x)](#sqrt(x))

+ [Base 7](#base-7)

+ [Largest Perimeter Triangle](#largest-perimeter-triangle)

+ [Fizz Buzz](#fizz-buzz)

## Palindrome Number

https://leetcode.com/problems/palindrome-number/


```python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        if 0 <= x <= 9:
            return True
        helper = x
        skip = 0
        cnt = 0
        while helper > 0:
            helper //= 10
            cnt += 1
        if cnt % 2 != 0:
            skip = 1
        cnt //= 2
        x1 = x // (10 ** (cnt + skip))
        x2 = x % (10 ** cnt)
        for i in range(1, cnt + 1):
            if x1 // (10 ** (cnt - 1)) != x2 % 10:
                return False
            x1 %= 10 ** (cnt - 1)
            x2 = (x2 - x2 % 10) // 10
            cnt -= 1
        return True

```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/


```python

class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        if n == len(fib) - 1:
            return fib[n]
        x = n  - len(fib)
        for _ in range(x + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]

```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/


```python

class Solution:
    def reverse(self, x: int) -> int:
        nums = []
        res = 0
        sign = 1
        neg = - 2**31
        pos = 2**31 - 1
        if x < 0:
            sign = -1
            x *= -1
        while x > 0:
            nums.append(x % 10)
            x //= 10
        for i, el in enumerate(nums):
            res += sign * el
            if res == 0 and el == 0:
                continue
            if i != len(nums) - 1:
                res *= 10
            if res > pos or res < neg:
                return 0
        return res

```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/


```python

class Solution:
    def binary_search(self, x, l, r):
        m = (l + r) // 2
        if m * m <= x:
            if (m + 1) ** 2 > x:
                return m
            else:
                return self.binary_search(x, m, r)
        else:
            return self.binary_search(x, l, m)


    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        return self.binary_search(x, 1, x + 1)

```

## Base 7

https://leetcode.com/problems/base-7/


```python

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        sign = ''
        if num < 0:
            sign = '-'
            num *= (-1)
        res = []
        result = ''
        while num >= 7:
            x = num // 7
            res.append(num - x * 7)
            num = x
        res.append(num)
        res = res[::-1]
        for el in res:
            result += str(el)
        result = sign + result
        return result

```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/


```python

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        res = 0
        i = 0
        A.sort(key=lambda x: -x)
        print(A)
        while i + 2 != len(A):
            if A[i] >= A[i + 1] + A[i + 2]:
                i += 1
            else:
                res = A[i] + A[i + 1] + A[i + 2]
                break
        return res






```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/


```python

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        result = []
        while i != n + 1:
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
            i += 1
        return result

```

