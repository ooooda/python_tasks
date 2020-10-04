# https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        if len(intervals) == 0 or len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        for i, el in enumerate(intervals):
            if i == 0:
                min_r = intervals[i][1]
            else:
                if el[0] < min_r:
                    result += 1
                else:
                    min_r = intervals[i][1]
        return result