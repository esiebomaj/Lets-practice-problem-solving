
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sizes = [((end-start)+1, start, end) for start, end in intervals]
        
        sizes.sort(key=lambda x:x[1])
        res = {}
        heap = []        
        i = 0
        # print(sizes)
        for q in sorted(queries):
            while i < len(sizes) and sizes[i][1] <= q:
                if sizes[i][1] <= q <= sizes[i][2]:
                    heapq.heappush(heap, sizes[i])
                i+=1
                
            while heap and heap[0][2] < q:
                heapq.heappop(heap)
            
            res[q] = heap[0][0] if heap else -1
        
        return [res[i] for i in queries]
            
                
        
        # print(sizes)
#         res = [-1]*len(queries)
        
#         for i,query in enumerate(queries):
#             for size, interval in sizes:
#                 if interval[0] <= query <= interval[1]:
#                     res[i]=size
#                     break

#         return res
            
            
        