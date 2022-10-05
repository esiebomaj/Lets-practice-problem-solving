class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = intervals[0]
        res = []
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if merged[1] < interval[0]:
                res.append(merged)
                merged = interval
            else:
                merged = [min(merged[0], interval[0]), max(merged[1], interval[1])]
                
        res.append(merged)
        
        return res