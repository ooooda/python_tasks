# dynamic-programming

+ [House Robber](#house-robber)

+ [House Robber II](#house-robber-ii)

## House Robber

https://leetcode.com/problems/house-robber/


```python

class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            if i == 0:
                num = nums[0]
            elif i == 1:
                num = max(nums[1], nums[0])
            else:
                num = max(ans[i-1], ans[i-2]+nums[i])
            ans.append(num)
        return ans[-1]

```

## House Robber II

https://leetcode.com/problems/house-robber-ii/


```python

class Solution:
    def robby(self, nums):
        ans = []
        for i in range(len(nums)):
            if i == 0:
                num = nums[0]
            elif i == 1:
                num = max(nums[1], nums[0])
            else:
                num = max(ans[i - 1], ans[i - 2] + nums[i])
            ans.append(num)
        return ans[-1]


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x = self.robby(nums[0:-1])
        y = self.robby(nums[1:])
        return max(x, y)

```

