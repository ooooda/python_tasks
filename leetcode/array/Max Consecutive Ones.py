# https://leetcode.com/problems/max-consecutive-ones/
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