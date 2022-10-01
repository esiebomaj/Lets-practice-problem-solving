class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        res = []
        
        for i in range(len(intervals)):
            interval = intervals[i]
            
            if newInterval[1] < interval[0]: # new interval is before Before
                return res + [newInterval] + intervals[i:]
            
            if newInterval[0] > interval[1]: # new interval is after
                res.append(interval)
                continue
            
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            
        res.append(newInterval)
        return res
            
            
            