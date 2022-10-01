class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        merged = intervals[0]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
        
            
            if not merged[1] < interval[0] and not merged[0] > interval[1]:
                # if overlap
                # we merge and continue 
                merged = [min(merged[0], interval[0]), max(merged[1], interval[1])]
                
            else:
                # if not overlap
                # we append merge 
                # reinitialize merge to interval 
                res.append(merged)
                merged = interval
                
            
        # append merge 
        res.append(merged)
        return res