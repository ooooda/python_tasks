# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for index, el in enumerate(nums):
            if el == 0:
                cnt += 1
            else:
                nums[index - cnt], nums[index] = nums[index], nums[index - cnt]