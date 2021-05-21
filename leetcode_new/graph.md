# graph

+ [Course Schedule](#course-schedule)

+ [Number of Islands](#number-of-islands)

+ [Course Schedule II](#course-schedule-ii)

+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)

+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)

+ [Is Graph Bipartite?](#is-graph-bipartite?)

+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)

## Course Schedule

https://leetcode.com/problems/course-schedule/


```python

class Solution:
    def __init__(self):
        self.vertices = []
        self.visited = []


    def cycle(self, arr):
        prior = {}
        for i in range(len(arr)):
            prior[arr[i]] = i
        for i, v in enumerate(self.vertices):
            for u in v:
                if prior[i] >= prior[u]:
                    return True
        return False


    def topologicalSort(self, v, ans):
        self.visited[v] = True
        for u in self.vertices[v]:
            if self.visited[u] == False:
                self.topologicalSort(u, ans)
        ans.append(v)


    def canFinish(self, num: int, courses: List[List[int]]) -> bool:
        self.visited = [False] * num
        self.vertices = [[] for _ in range(num)]
        for i in range(len(courses)):
            index = courses[i][1]
            v = courses[i][0]
            self.vertices[index].append(v)
        ans = []
        print(self.vertices)
        for u in range(len(self.vertices)):
            if not self.visited[u]:
                self.topologicalSort(u, ans)
        ans = ans[::-1]
        if self.cycle(ans):
            ans = []
        return len(ans) != 0




```

## Number of Islands

https://leetcode.com/problems/number-of-islands/


```python

class Solution:
    def decrease_1(self, arr, i, j, n, m):
        if arr[i][j] == "1":
            arr[i][j] = "0"
            if i < n - 1:
                self.decrease_1(arr, i + 1, j, n, m)
            if i > 0:
                self.decrease_1(arr, i - 1, j, n, m)
            if j < m - 1:
                self.decrease_1(arr, i, j + 1, n, m)
            if j > 0:
                self.decrease_1(arr, i, j - 1, n, m)


    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        num = 0
        index = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    num += 1
                    self.decrease_1(grid, i, j, n, m)
        return num


```

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/


```python

class Solution:
    def __init__(self):
        self.vertices = []
        self.visited = []


    def cycle(self, arr):
        prior = {}
        for i in range(len(arr)):
            prior[arr[i]] = i
        for i, v in enumerate(self.vertices):
            for u in v:
                if prior[i] >= prior[u]:
                    return True
        return False


    def topologicalSort(self, v, ans):
        self.visited[v] = True
        for u in self.vertices[v]:
            if self.visited[u] == False:
                self.topologicalSort(u, ans)
        ans.append(v)


    def findOrder(self, num: int, courses: List[List[int]]) -> List[int]:
        self.visited = [False] * num
        self.vertices = [[] for _ in range(num)]
        for i in range(len(courses)):
            index = courses[i][1]
            v = courses[i][0]
            self.vertices[index].append(v)
        ans = []
        print(self.vertices)
        for u in range(len(self.vertices)):
            if not self.visited[u]:
                self.topologicalSort(u, ans)
        ans = ans[::-1]
        if self.cycle(ans):
            return []
        return ans






```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/


```python

from collections import deque


class Solution:
    def bfs(self, grid):
        q = deque()
        n = len(grid) - 1
        q.append((0, 0, 1))
        while len(q) > 0:
            x, y, way = q.popleft()
            X = [0]
            Y = [0]
            if x > 0:
                X.append(-1)
            if x < n:
                X.append(+1)
            if y > 0:
                Y.append(-1)
            if y < n:
                Y.append(+1)
            for x_i in X:
                for y_j in Y:
                    if grid[x_i + x][y_j + y] == 0:
                        if x_i ** 2 + y_j ** 2 != 0:
                            q.append((x_i + x, y_j + y, way + 1))
                        grid[x_i + x][y_j + y] = 1
            if x == y and x == n:
                return way
        return -1


    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        return self.bfs(grid)

```

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/


```python

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if len(root.children) == 0:
            return 1
        level = 0
        for i in root.children:
            l = self.maxDepth(i)
            if l + 1 > level:
                level = l + 1
        return level






```

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/


```python

class Solution:
    def __init__(self):
        self.wrong_colour = False


    def dfs(self, v, c, graph, colours):
        colours[v] = c
        c = c ^ 1
        for u in graph[v]:
            if colours[u] is not None:
                if colours[u] != c:
                    self.wrong_colour = True
            else:
                self.dfs(u, c, graph, colours)


    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) <= 2:
            return True
        length = len(graph)
        colours = [None] * length
        for i in range(length):
            if colours[i] is None:
                self.dfs(i, 0, graph, colours)
        return not self.wrong_colour

```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/


```python

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k += 2
        graph = [[]for _ in range(n)]
        for el in flights:
            graph[el[0]].append(el[1:])
        inf = 1e9
        prices = [[inf]*n for _ in range(k)]
        prices[0][src] = 0
        for i in range(1, k):
            for j in range(n):
                prices[i][j] = prices[i-1][j]
            for u, v, w in flights:
                prices[i][v] = min(prices[i][v], prices[i-1][u] + w)
        if prices[k-1][dst] == inf:
            return -1
        return prices[k-1][dst]

```

