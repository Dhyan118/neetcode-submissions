class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prvEnd = intervals[0][1] #first interval end time

        for start, end in intervals[1:]:
            if start >= prvEnd:
                prvEnd = end
            else:
                res += 1
                prvEnd = min(end, prvEnd)
        return res