from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finder = set()
        first = 0
        second = 0
        status = True
        result = []
        index1 = -1
        index2 = -1
        for el in nums:
            finder.add(el)

        for i in range(len(nums)):
            if status:
                if target - nums[i] in finder:
                    if nums[i] != target - nums[i]:
                        first = target - nums[i]
                        second = nums[i]
                        status = False
                        continue
                    else:
                        finder.remove(nums[i])
                        if len(nums) - len(finder) > 1:
                            first = nums[i]
                            second = nums[i]
                            status = False
                            continue

        for i, el in enumerate(nums):
            if first == second:
                if el == first and len(result) < 2:
                    result.append(i)
            else:
                if el == first:
                    index1 = i
                if el == second:
                    index2 = i

        if len(result) == 0:
            result.append(index1)
            result.append(index2)

        return result


if __name__ == '__main__':
    print(Solution().twoSum([1, 3, 5, 6, 2, 6], 4))