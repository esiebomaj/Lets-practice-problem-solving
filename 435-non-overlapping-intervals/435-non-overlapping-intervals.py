class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        intercept = intervals[0]
        count = 0
        
        for interval in intervals[1:]:
            if intercept[1] <= interval[0]:
                # no interception
                intercept = interval
            else:
                count += 1
                intercept = [max(intercept[0], interval[0]), min(intercept[1], interval[1])]
        
        return count
                