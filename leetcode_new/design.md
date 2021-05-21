# design

+ [Min Stack](#min-stack)

+ [Implement Queue using Stacks](#implement-queue-using-stacks)

+ [Design Twitter](#design-twitter)

+ [Implement Stack using Queues](#implement-stack-using-queues)

## Min Stack

https://leetcode.com/problems/min-stack/


```python

class MinStack:


    def __init__(self):
        self.m = None
        self.nums = []


    def push(self, val: int) -> None:
        if self.m is None:
            self.m = val
        else:
            if val < self.m:
                self.m = val
        self.nums.append(val)


    def pop(self) -> None:
        val = self.nums[-1]
        self.nums.pop(-1)
        if val == self.m:
            if len(self.nums) == 0:
                self.m = None
            else:
                self.m = self.nums[0]
                for el in self.nums:
                    if el < self.m:
                        self.m = el


    def top(self) -> int:
        return self.nums[-1]


    def getMin(self) -> int:
        return self.m




```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/


```python

class MyQueue:
    def check_down(self):
        if len(self.down) == 0:
            self.down = self.up[::-1]
            self.up = []


    def __init__(self):
        self.up = []
        self.down = []


    def push(self, x: int) -> None:
        self.up.append(x)


    def pop(self) -> int:
        self.check_down()
        num = self.down[-1]
        self.down.pop(-1)
        return num


    def peek(self) -> int:
        self.check_down()
        num = self.down[-1]
        return num


    def empty(self) -> bool:
        if len(self.up) == len(self.down) and len(self.up) == 0:
            return True
        return False


```

## Design Twitter

https://leetcode.com/problems/design-twitter/


```python

from collections import deque
from collections import defaultdict




class Twitter:


    def get10resent(self, user):
        if len(self._tweet[user]) <= 10:
            return
        while len(self._tweet[user]) != 10:
            self._tweet[user].popleft()


    def __init__(self):
        self._followee = defaultdict(set)
        # self._followers = defaultdict(set)
        self._tweet = defaultdict(list)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self._tweet[userId].append((tweetId, self.time))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = []
        for f in self._followee[userId]:
            tweets.extend(self._tweet[f][-10:])
        tweets.extend(self._tweet[userId])
        tweets = sorted(tweets, key=lambda x: x[1])
        cleaned = []
        for t in tweets[-10:]:
            cleaned.append(t[0])


        return cleaned[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self._followee[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self._followee:
            if followeeId in self._followee[followerId]:
                self._followee[followerId].remove(followeeId)


```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/


```python

from collections import deque




class MyStack:
    def check_length(self):
        if len(self.q1) >= (len(self.q1)) ** 0.5:
            while len(self.q2) != 0:
                el = self.q2.popleft()
                self.q1.append(el)
        self.q1, self.q2 = self.q2, self.q1


    def cycle(self):
        for _ in range(len(self.q1) - 1):
            el = self.q1.popleft()
            self.q1.append(el)


    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        self.check_length()
        self.q1.append(x)
        self.cycle()


    def pop(self) -> int:
        if len(self.q1) != 0:
            return self.q1.popleft()
        return self.q2.popleft()


    def top(self) -> int:
        copy1 = self.q1.copy()
        copy2 = self.q2.copy()
        if len(copy1) != 0:
            return copy1.popleft()
        return copy2.popleft()


    def empty(self) -> bool:
        if len(self.q1) == 0 and len(self.q1) == len(self.q2):
            return True
        return False


```

