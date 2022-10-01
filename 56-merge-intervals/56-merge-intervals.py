class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        merged = intervals[0]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
        
            #if overlap
            # we merge and continue 
            if not merged[1] < interval[0] and not merged[0] > interval[1]:
                merged = [min(merged[0], interval[0]), max(merged[1], interval[1])]
            else:
                res.append(merged)
                merged = interval
                
            
            # if not overlap
            # we append merge 
            # reinitialize merge to interval 
            
            
        # append merge 
        res.append(merged)
        return res