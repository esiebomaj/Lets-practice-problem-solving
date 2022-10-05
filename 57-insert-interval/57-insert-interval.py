class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        
        for i in range(len(intervals)):
            interval = intervals[i]
            
            if interval[0] > newInterval[1]:
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            elif interval[1] < newInterval[0]:
                newIntervals.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                
        newIntervals.append(newInterval)
        return newIntervals
                
        