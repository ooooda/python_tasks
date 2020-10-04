# https://leetcode.com/problems/insert-interval/
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