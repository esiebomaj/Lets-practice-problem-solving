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
        # Notes: heapq uses the first item in a turple to compare
        # if the first item is equal it moves on to break the tie using the second item in the turple
        # hence this is not stable as you are not assured that the order of tied items will be the same as their order in the input
        # to make heapsort stable we can have a tuple of 3 items, the first is the main comparisom object, 
        # the second item be the order they appear in the input (incase of a tie - it will compare using this value - making it stable) 
        # and the third item can be any other thing
        
        res = []
        
        for i in range(k): # O(k)
            res.append(heapq.heappop(points)[1]) #O(logn)
        
        return res
        
            
        