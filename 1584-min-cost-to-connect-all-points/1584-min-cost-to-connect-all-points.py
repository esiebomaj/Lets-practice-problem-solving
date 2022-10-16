import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def manhattan(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
#         memo = {}
        
#         def getDist(p1, p2):
#             combined = tuple(sorted((str(p1[0]) + str(p1[1]), str(p2[0]) + str(p2[1]))))
#             if combined not in memo:
#                 memo[combined] = manhattan(p1,p2)
                
#             return memo[combined] 
        
        
        p1 = points[0]
        q = [(0, p1[0], p1[1])]
        seen = set()
        
        res = 0
        
        while q:
            if len(seen) == len(points):
                return res
            
            curr = heapq.heappop(q)
            if (curr[1], curr[2]) not in seen:
                seen.add((curr[1], curr[2]))
                res += curr[0] 
                for p in points:
                    d = manhattan((curr[1], curr[2]), p)
                    heapq.heappush(q, (d, p[0], p[1]))
                                           
        return res