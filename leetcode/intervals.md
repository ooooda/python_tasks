# intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)

+ [Merge Intervals](#merge-intervals)

+ [Insert Interval](#insert-interval)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/


```python

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        if len(intervals) == 0 or len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        for i, el in enumerate(intervals):
            if i == 0:
                min_r = intervals[i][1]
            else:
                if el[0] < min_r:
                    result += 1
                else:
                    min_r = intervals[i][1]
        return result

```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/


```python

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        for i, el in enumerate(intervals):
            if i == 0:
                result.append(el)
            else:
                if el[0] > result[-1][1]:
                    result.append(el)
                else:
                    if result[-1][1] < el[1]:
                        result[-1][1] = el[1]
        return result

```

## Insert Interval

https://leetcode.com/problems/insert-interval/


```python

class Solution:
    def merger(self, intervals):
        result = []
        intervals.sort(key=lambda x: x[0])
        for i, el in enumerate(intervals):
            if i == 0:
                result.append(el)
            else:
                if el[0] > result[-1][1]:
                    result.append(el)
                else:
                    if result[-1][1] < el[1]:
                        result[-1][1] = el[1]
        return result


    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        intervals.append(new)
        result = self.merger(intervals)
        return result

```

