# https://leetcode.com/problems/reshape-the-matrix/
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

