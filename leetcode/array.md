# array

+ [Move Zeroes](#move-zeroes)

+ [Reshape the Matrix](#reshape-the-matrix)

+ [Flipping an Image](#flipping-an-image)

+ [Max Consecutive Ones](#max-consecutive-ones)

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

+ [Image Smoother](#image-smoother)

+ [Transpose Matrix](#transpose-matrix)

## Move Zeroes

https://leetcode.com/problems/move-zeroes/


```python

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for index, el in enumerate(nums):
            if el == 0:
                cnt += 1
            else:
                nums[index - cnt], nums[index] = nums[index], nums[index - cnt]

```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/


```python

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r == c and c == 0 or len(nums) == 0:
            return nums
        pos_res = r * c
        cnt = 0
        row = []
        helper = []
        i = c
        for el in nums:
            cnt += len(el)
            row += (el)
        if cnt != pos_res:
            return nums
        nums = []
        for index, el in enumerate(row):
            if i != 0:
                i -= 1
                helper.append(el)
            if i == 0 or index == len(row) - 1:
                i = c
                nums.append(helper)
                helper = []
        return nums




```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/


```python

class Solution:
    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        for i, el in enumerate(a):
            a[i] = el[::-1]
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 1:
                    a[i][j] = 0
                    continue
                else:
                    a[i][j] = 1
                    continue
        return a

```

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/


```python

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        helper = 0
        if len(nums) != 0:
            for el in nums:
                if el == 1:
                    helper += 1
                else:
                    helper = 0
                cnt = max(cnt, helper)
        return cnt

```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/


```python

class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        if len(a) != 0:
            a = sorted(a, key = lambda x: abs(x))
            for i in range(len(a)):
                a[i] = a[i] * a[i]
        return a

```

## Image Smoother

https://leetcode.com/problems/image-smoother/


```python

from copy import deepcopy


class Solution:
    def imageSmoother(self, a: List[List[int]]) -> List[List[int]]:
        if len(a) == 0:
            return a
        res = deepcopy(a)
        for i, el in enumerate(a):
            for j, elem in enumerate(el):
                s = elem
                cnt = 1
                if i != 0:
                    s += a[i - 1][j]
                    cnt += 1
                    if j != 0:
                        s += a[i - 1][j - 1]
                        cnt += 1
                    if j != len(el) - 1:
                        s += a[i - 1][j + 1]
                        cnt += 1
                if j != 0:
                    s += a[i][j - 1]
                    cnt += 1
                if j != len(el) - 1:
                    s += a[i][j + 1]
                    cnt += 1
                if i != len(a) - 1:
                    s += a[i + 1][j]
                    cnt += 1
                    if j != 0:
                        s += a[i + 1][j - 1]
                        cnt += 1
                    if j != len(el) - 1:
                        s += a[i + 1][j + 1]
                        cnt += 1
                res[i][j] = s // cnt
        return res




```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/


```python

class Solution:
    def transpose(self, a: List[List[int]]) -> List[List[int]]:
        if len(a) == 0:
            return a
        c = 0
        i = 0
        j = 0
        helper = []
        for _ in a:
            c += 1
        r = len(a[0])
        res = []
        while i != r:
            if j != c:
                helper.append(a[j][i])
                j += 1
            else:
                j = 0
                res.append(helper)
                helper = []
                i += 1
        return res

```

