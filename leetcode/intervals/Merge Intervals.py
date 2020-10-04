# https://leetcode.com/problems/merge-intervals/
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