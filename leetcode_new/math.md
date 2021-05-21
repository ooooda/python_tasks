# math

+ [K Closest Points to Origin](#k-closest-points-to-origin)

## K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/


```python

class Solution:
    def counter(self, x, y):
        return x ** 2 + y ** 2


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for i, el in enumerate(points):
            x, y = el
            points[i] = [self.counter(x, y), x, y]
        points.sort(key=lambda x: x[0])
        for i in range(k):
            result.append([points[i][1], points[i][2]])
        return result

```

