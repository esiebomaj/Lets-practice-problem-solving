import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        i = 0
        heap = []
        intervals.sort()
        res = {}
        
        for q in sorted(queries):
            
            while i < len(intervals) and q >= intervals[i][0]:
                interval = intervals[i]
                left = interval[0]
                right = interval[1]
                size = right - left + 1
                heapq.heappush(heap, [size, left, right])
                i += 1
            
            while heap and q > heap[0][2]:
                heapq.heappop(heap)
                
            # print(heap)  
            res[q] = heap[0][0] if heap else -1
            
        return [res[i] for i in queries]