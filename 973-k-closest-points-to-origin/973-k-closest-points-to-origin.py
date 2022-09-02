import math

class Pair:
    def __init__(self, distance, coord):
        self.distance = distance
        self.coord = coord
    def __repr__(self,):
        return f"{self.distance}|{self.coord}"
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)): #O(n)
            point = points[i]
            d = math.sqrt((point[0]*point[0]) + (point[1]*point[1]))
            points[i] = Pair(d, point)
            
        points = sorted(points, key=lambda x:x.distance, reverse=True) # O(nlogn)
        
        res = []
        for i in range(k): # O(n)
            res.append(points.pop().coord)
        
        return res
        
            
        