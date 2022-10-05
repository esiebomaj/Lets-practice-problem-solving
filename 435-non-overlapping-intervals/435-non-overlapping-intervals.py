class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        intercept = intervals[0]
        count = 0
        
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] >= intercept[1]:
                # no overlap with intercept
                intercept = interval
            else:
                # overlap with intercept
                count += 1
                intercept = [max(intercept[0], interval[0]), min(intercept[1], interval[1])]
        
        return count