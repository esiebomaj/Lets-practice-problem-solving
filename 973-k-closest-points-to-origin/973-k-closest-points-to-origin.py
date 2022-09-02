import math
import heapq

class Pair:
    def __init__(self, distance, coord):
        self.distance = distance
        self.coord = coord
    def __repr__(self,):
        return f"{self.distance}|{self.coord}"
        
class Solution:
    # my brute force solution using sorting
    # Time: O(NlogN) 
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         for i in range(len(points)): #O(n)
#             point = points[i]
#             d = math.sqrt((point[0]*point[0]) + (point[1]*point[1]))
#             points[i] = Pair(d, point)
            
#         points = sorted(points, key=lambda x:x.distance, reverse=True) # O(nlogn)
        
#         res = []
#         for i in range(k): # O(n)
#             res.append(points.pop().coord)
        
#         return res


    # Optimized solution using a heap instead of sorting
    # Time: O(KlogN)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)): #O(n)
            point = points[i]
            d = math.sqrt((point[0]*point[0]) + (point[1]*point[1]))
            points[i] = (d, point)
            
        heapq.heapify(points) #O(n)
        
        res = []
        
        for i in range(k): # O(k)
            res.append(heapq.heappop(points)[1]) #O(logn)
        
        return res
        
            
        